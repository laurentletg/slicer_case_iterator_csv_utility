import os
import glob
import pandas as pd
import argparse

ROOT = os.path.join(os.getcwd(), 'data')

def get_args():
    parser = argparse.ArgumentParser(description='Generate a csv file for Slicer case iterator')
    parser.add_argument('--path', type=str, default=ROOT, help='Path to the folder containing the images, masks and gts')
    parser.add_argument('--images', type=str, default='image', help='Name of the folder containing the images')
    parser.add_argument('--masks', type=str, default='mask', help='Name of the folder containing the masks')
    parser.add_argument('--gts', type=str, default='gt', help='Name of the folder containing the ground truth')
    parser.add_argument('--extension', type=str, default='nrrd', help='Extension of the files')
    args = parser.parse_args()
    return args

def get_rel_path(root_dir, input_dir, extension):
    full_path = os.path.join(root_dir, input_dir)
    try:
        assert os.path.exists(full_path)
    except AssertionError:
        print(f'{full_path} does not exist')
        return []
    
    try: 
        paths = glob.glob(os.path.join(full_path, '**', f'*.{extension}'), recursive=True)
        print(f'Found {len(paths)} {extension} files in {full_path}')
    except IndexError:
        print(f'No {extension} files in {full_path}')
        return []
    
    rel_paths = [os.path.relpath(path, root_dir) for path in paths]
    return rel_paths

def get_df(dictionary, root_dir):
    df = pd.DataFrame(dictionary)
    df['path'] = root_dir
    return df

def main():
    args = get_args()
    print(f'Looking in root directory : {args.path}')
    images = get_rel_path(args.path, args.images, args.extension)
    masks = get_rel_path(args.path, args.masks, args.extension)
    gts = get_rel_path(args.path, args.gts, args.extension)
    
    if not (images and masks and gts):
        print("Error: One or more directories are empty or do not exist.")
        return
    
    if len(images) != len(masks) or len(images) != len(gts):
        print('Warning: Not the same number of images, masks and gts')
        print(f'Images: {len(images)}, Masks: {len(masks)}, GTs: {len(gts)}')
    else:
        print(f'Same number of files in each category: {len(images)}')
    
    data = {
        'image': images, 
        'mask': masks,
        'gt': gts
    }
    df = get_df(data, args.path)
    output_file = 'slicer_case_iterator_input.csv'
    df.to_csv(output_file, index=False)
    print(50 * '-')
    print('CSV generated')
    print(f'CSV available here: {os.path.abspath(output_file)}')
    print(f'CSV name: {output_file}')
    print('Load the csv directly (drag and drop) in Slicer as a table node')
    print(50 * '-')
    
if __name__ == '__main__':
    main()