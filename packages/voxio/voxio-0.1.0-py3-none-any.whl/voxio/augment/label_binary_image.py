import pickle
from collections import deque, defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Iterable, Sequence

import cv2
import imagesize
import numpy as np
from numba import njit
from pydantic import FilePath, DirectoryPath, validate_arguments
from pydantic_numpy import NDArray
from scipy import ndimage

from voxio.read import simple_read_images, parallel_scan_stack_images, cv2_read_binary_image, chunk_read_stack_images
from voxio.utils.misc import (
    sort_indexed_dict_keys_to_value_list,
    write_indexed_images_to_directory,
    high_compression_png_save,
    number_of_planes_loadable_to_memory,
)
from voxio.utils.typings import TupleSlice


@validate_arguments
def label_binary_image(image_paths: tuple[FilePath, ...], output_directory: DirectoryPath) -> None:
    def volume_save_path(volume_index: int) -> Path:
        return cache_dir / f"{volume_index}.npz"

    volume_index, current_max_image_id = 0, 0
    # tuple[old, new]
    pidx_to_must_map_later: dict[int, set[tuple[int, int]]] = defaultdict(list)

    cache_dir = output_directory / "cache"
    cache_dir.mkdir(parents=True, exist_ok=True)

    image_generator = chunk_read_stack_images(
        image_paths,
        cv2_read_binary_image,
        chunk_size=number_of_planes_loadable_to_memory(imagesize.get(image_paths[0]), memory_tolerance=0.3, byte_mul=4),
    )

    queue, image_id_ranges = deque(), []
    while image_generator:
        if queue:
            np.savez(str(volume_save_path(volume_index - 2)), v=queue.popleft())
        while len(queue) < 2:
            volume_index += 1
            image_id_ranges.append(current_max_image_id)

            upcoming = ndimage.label(next(image_generator))[0].astype(np.uint16)
            queue.append(upcoming)
            current_max_image_id += len(upcoming)
        del upcoming

        first_argwhere = queue[1] != 0
        queue[1][first_argwhere] = queue[1][first_argwhere] + np.max(queue[0])
        del first_argwhere

        bottom_plane_1st = queue[0][-1]

        top_plane_2nd = queue[1][0]
        top_objects = ndimage.find_objects(top_plane_2nd)

        max_on_first = np.max(queue[1])
        previous_first_pidx = volume_index - 3

        for object_slices in top_objects:
            if not object_slices:
                continue
            slice_of_previous_plane = bottom_plane_1st[object_slices]
            if not np.any(slice_of_previous_plane):
                continue

            overlapping_labels = deque(np.unique(slice_of_previous_plane))
            if overlapping_labels[0] == 0:
                overlapping_labels.popleft()

            if not overlapping_labels:
                continue

            unique_on_2nd_top_object_slice = np.unique(top_plane_2nd[object_slices])
            match len(unique_on_2nd_top_object_slice):
                case 1:
                    old_label_on_first = unique_on_2nd_top_object_slice[0]
                    assert old_label_on_first != 0
                case 2:
                    old_label_on_first = unique_on_2nd_top_object_slice[1]
                case _:
                    raise ValueError("Too many labels on the object slice")

            first = overlapping_labels.pop()
            queue[1][queue[1] == old_label_on_first] = first
            queue[1][queue[1] == max_on_first] = old_label_on_first
            max_on_first -= 1

            for overlapping_label in overlapping_labels:
                if overlapping_label in queue[0][0] and previous_first_pidx >= 0:
                    pidx_to_must_map_later[previous_first_pidx].add((overlapping_label, first))
                queue[0][queue[0] == overlapping_label] = first

    indices_to_export: set[int] = set(range(volume_index + 1))
    write_indexed_images_to_directory(output_directory, queue.pop(), naming_index_start=image_id_ranges.pop())
    indices_to_export.remove(volume_index)
    del queue

    """
    We need to scan backwards after we are done, and let newer jobs trickle down.
    By not scanning from the bottom we ensure we only load little volumes as possible
    """

    for plane_idx, to_map_records in sorted(pidx_to_must_map_later.items(), reverse=True):
        array = np.load(str(volume_save_path(plane_idx)))["v"]
        for old, new in to_map_records:
            if old in array[0] and plane_idx > 0:
                pidx_to_must_map_later[plane_idx - 1].add((old, new))
            array[array == old] = new
        write_indexed_images_to_directory(output_directory, array, naming_index_start=image_id_ranges[plane_idx])
        indices_to_export.remove(plane_idx)

    for idx_to_export in indices_to_export:
        write_indexed_images_to_directory(
            output_directory,
            np.load(str(volume_save_path(idx_to_export)))["v"],
            naming_index_start=image_id_ranges[idx_to_export],
        )
