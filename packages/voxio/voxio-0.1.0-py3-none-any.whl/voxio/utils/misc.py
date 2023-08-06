from concurrent.futures import ThreadPoolExecutor
from math import floor
from pathlib import Path
from typing import Callable, Sequence, Iterable, Any, Optional

import cv2
import numpy as np
import psutil
from pydantic import DirectoryPath, FilePath, validate_arguments
from pydantic_numpy import NDArray


@validate_arguments
def get_image_paths(image_directory: DirectoryPath, image_format: str, sorting_key: Callable) -> Iterable[FilePath]:
    assert image_directory.is_dir()

    file_filter = f"*.{image_format}" if image_format else "*.*"
    return sorted(image_directory.glob(file_filter), key=sorting_key)


@validate_arguments
def number_of_planes_loadable_to_memory(
    plane_shape: Sequence[int], memory_tolerance: float = 1.0, byte_mul: int = 1
) -> int:
    return floor(psutil.virtual_memory().available * memory_tolerance / (np.multiply.reduce(plane_shape) * byte_mul))


def sort_indexed_dict_keys_to_value_list(key_index_dict: dict[float, Any]) -> list:
    return [v for _k, v in sorted(key_index_dict.items(), key=lambda kv: kv[0])]


def high_compression_png_save(image: NDArray, out_path: Path) -> None:
    assert out_path.suffix == ".png"
    cv2.imwrite(str(out_path), image, [cv2.IMWRITE_PNG_COMPRESSION, 9])


def write_indexed_images_to_directory(
    output_directory: DirectoryPath, images: Iterable[NDArray], naming_index_start: int = 0
) -> None:
    with ThreadPoolExecutor() as executor:
        for image_index, image_plane in enumerate(images, start=naming_index_start):
            executor.submit(high_compression_png_save, image_plane, output_directory / f"{image_index}.png")
