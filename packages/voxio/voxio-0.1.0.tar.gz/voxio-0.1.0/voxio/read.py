from concurrent.futures import ThreadPoolExecutor
from logging import getLogger
from math import floor, ceil
from pathlib import Path
from typing import Callable, Generator, Iterable, Optional, Sequence

import cv2
import imagesize
import numpy as np
from pydantic import FilePath
from pydantic_numpy import NDArrayUint8, NDArrayUint16

from voxio.utils.misc import number_of_planes_loadable_to_memory

logger = getLogger(__name__)


def read_stack_images(
    image_paths: Sequence[FilePath],
    image_reader: Callable[[Path | str], np.ndarray],
    parallel: bool = True,
) -> np.ndarray:
    return (
        parallel_read_stack_images(image_paths, image_reader)
        if parallel
        else np.array([image_reader(img_path) for img_path in image_paths])
    )


def simple_read_images(image_paths: Sequence[FilePath], parallel: bool = True) -> np.ndarray:
    return read_stack_images(image_paths, cv2_read_any_depth, parallel)


def chunk_read_stack_images(
    image_paths: Sequence[FilePath],
    image_reader: Callable[[Path | str], np.ndarray],
    chunk_size: Optional[int] = None,
    parallel: bool = True,
) -> Generator[np.ndarray, None, None]:
    chunks = []
    start, stop = 0, chunk_size
    while stop < len(image_paths):
        chunks.append(image_paths[start:stop])
        start = stop
        stop += chunk_size
    chunks.append(image_paths[start:])

    for image_paths_chunk in chunks:
        yield (
            parallel_read_stack_images(image_paths_chunk, image_reader)
            if parallel
            else np.array([image_reader(img_path) for img_path in image_paths_chunk])
        )


def parallel_read_stack_images(image_paths: Iterable[Path], image_reader: Callable):
    with ThreadPoolExecutor() as executor:
        return np.array([image for image in executor.map(image_reader, image_paths)])


def parallel_scan_stack_images(image_paths: Sequence[Path], image_reader: Callable, with_index: bool = False):
    map_args = [image_reader, image_paths]
    if with_index:
        map_args.append(range(len(image_paths)))

    with ThreadPoolExecutor() as executor:
        executor.map(*map_args)


def cv2_read_any_depth(image_path: FilePath) -> np.ndarray:
    return cv2.imread(str(image_path), cv2.IMREAD_ANYDEPTH)


def cv2_read_binary_image(image_path: FilePath) -> NDArrayUint8:
    return cv2.imread(str(image_path), cv2.IMREAD_UNCHANGED).astype(np.uint8)


def cv2_read_uint16(image_path: FilePath) -> NDArrayUint16:
    return cv2.imread(str(image_path), cv2.IMREAD_UNCHANGED).astype(np.uint16)


def read_binarize_rgb(image_path: FilePath) -> np.ndarray:
    return np.any(cv2.imread(str(image_path)), axis=-1)
