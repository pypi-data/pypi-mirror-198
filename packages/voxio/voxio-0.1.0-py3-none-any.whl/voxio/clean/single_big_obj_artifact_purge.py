from concurrent.futures import ThreadPoolExecutor
from logging import getLogger

import cv2
import numpy as np
from pydantic import DirectoryPath, FilePath, validate_arguments
from scipy import ndimage
from scipy.ndimage import find_objects

from voxio.read import chunk_read_stack_images, cv2_read_any_depth
from voxio.utils.misc import high_compression_png_save

logger = getLogger(__name__)


def _volume_from_slices(*slices: slice) -> int:
    volume = 1
    for comp_slice in slices:
        volume *= comp_slice.stop - comp_slice.start
    return volume


def _read_and_purge_small_artifacts(image_volume: np.ndarray) -> np.ndarray[bool, bool]:
    labeled, num_features = ndimage.label(image_volume)

    object_slice_sequence = find_objects(labeled)
    size_to_label = {
        _volume_from_slices(*slices): label for label, slices in zip(range(1, num_features + 1), object_slice_sequence)
    }
    max_label = size_to_label[max(size_to_label)]

    result = labeled[object_slice_sequence[max_label - 1]] == max_label
    assert np.any(result)
    return result


@validate_arguments
def clear_everything_but_largest_object(image_paths: tuple[FilePath], output_directory: DirectoryPath) -> None:
    image_index = 0
    for cleaned_image_stack in chunk_read_stack_images(image_paths, cv2_read_any_depth):
        with ThreadPoolExecutor() as executor:
            for image in cleaned_image_stack:
                executor.submit(high_compression_png_save, image, output_directory / f"{image_index}.png")
                image_index += 1
