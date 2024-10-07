# Slicer Case Iterator CSV Generator

This Python script generates a CSV file for use with the Slicer Case Iterator module. It processes image, mask, and ground truth files from specified directories and creates a CSV file that can be directly loaded into Slicer as a table node.

## Requirements

- Python 3.x
- Dependencies listed in `requirements.txt`


## Expected data (volumes & masks) input
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

## Installation

You can set up the environment using either venv or Conda. Choose the option that best suits your workflow.

### Option 1: Using venv

1. Clone this repository or download the script.

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

### Option 2: Using Conda

1. Clone this repository or download the script.

2. Create a new Conda environment:
   ```
   conda create --name slicer-case-iterator python=3.x
   ```
   Replace `3.x` with your preferred Python version (e.g., 3.8, 3.9, etc.)

3. Activate the Conda environment:
   ```
   conda activate slicer-case-iterator
   ```

4. Install the required packages:
   ```
   conda install --file requirements.txt
   ```
   
   If some packages are not available via Conda, you can install them using pip within the Conda environment:
   ```
   pip install -r requirements.txt
   ```

Note: The `requirements.txt` file is already available in the repository.

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

## Output

The script generates a CSV file named 'slicer_case_iterator_input.csv' in the current working directory. This file can be directly loaded into Slicer as a table node (drag and drop).


