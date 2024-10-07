# Slicer Case Iterator CSV Generator

This Python script generates a CSV file for use with the Slicer Case Iterator module. It processes image, mask, and ground truth files from specified directories and creates a CSV file that can be directly loaded into Slicer as a table node.

## Requirements

- Python 3.x
- pandas

## Installation

1. Clone this repository or download the script.
2. Install the required packages:

```
pip install pandas
```

## Usage

Run the script from the command line with optional arguments:

```
python script_name.py [--path PATH] [--images IMAGES] [--masks MASKS] [--gts GTS] [--extension EXTENSION]
```

### Arguments

- `--path`: Path to the folder containing the images, masks, and ground truths (default: current working directory + '/data')
- `--images`: Name of the folder containing the images (default: 'image')
- `--masks`: Name of the folder containing the masks (default: 'mask')
- `--gts`: Name of the folder containing the ground truths (default: 'gt')
- `--extension`: File extension of the images, masks, and ground truths (default: 'nrrd')

## Expected input
Make sure that the folder structure and file naming conventions are consistent for the script to work correctly.
```
├── gt
│   ├── gt_01.seg.nrrd
│   └── gt_05.seg.nrrd
├── image
│   ├── vol_01.nrrd
│   └── vol_05.nrrd
└── mask
    ├── mask_01.seg.nrrd
    └── mask_05.seg.nrrd
```


## Output

The script generates a CSV file named 'slicer_case_iterator_input.csv' in the current working directory. This file can be directly loaded into Slicer as a table node (drag and drop).

## Error Handling

- The script will print an error message if the specified directories do not exist.
- It will also print an error message if there are no files with the specified extension in the directories.
- An assertion error is raised if the number of images, masks, and ground truths are not the same.

