# Voxio: I/O package for 3D images

## Usage
- Read images in parallel with `simple_read_images(image_paths)`
- Read volumes that would require more than system memory in chunks, use reader to perform compute/analysis `chunk_read_stack_images(image_paths,  image_reader)`
- Remove artifacts from volume with single object `clear_everything_but_largest_object(image_paths, output_directory)`
- Interpolate along the first dimension (z-axis) `morphological_interpolation_max_resolution_spacing(labeled_stack, ceiled_inter_stack_voxel_distance)`

## Installation
```shell
pip install voxio
```