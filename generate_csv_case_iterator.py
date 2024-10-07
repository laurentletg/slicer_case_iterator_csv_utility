import os, glob
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
    try:
        assert os.path.exists(os.path.join(root_dir, input_dir))
    except AssertionError:
        print(f'{input_dir} does not exist in {root_dir}')
    try: 
        paths = glob.glob(os.path.join(input_dir, '**', f'*.{extension}'), recursive=True)
    except IndexError:
        print(f'No {extension} files in {input_dir}')
    paths = [os.path.relpath(i, input_dir) for i in paths]
    return paths

def get_df(dictionnary, root_dir):
    df = pd.DataFrame(dictionnary)
    df['path'] = root_dir
    return pd.DataFrame(dictionnary)


def main():
    args = get_args()
    images = get_rel_path(args.path, args.images, args.extension)
    masks = get_rel_path(args.path, args.masks, args.extension)
    gts = get_rel_path(args.path, args.gts, args.extension)
    try:
        assert len(images) == len(masks) == len(gts)
        print(f'Same number of images {len(images)}')
    except AssertionError:
        print('Not the same number of images, masks and gts')
    
    data = {
        'image':images, 
        'mask':masks,
        'gt':gts
    }
    df = get_df(data, args.path)
    df.to_csv('slicer_case_iterator_input.csv')
    print(50 * '-')
    print('CSV generated')
    print(f'CSV available here : {os.getcwd()}')
    print('Load the csv directly (drag and drop) in Slicer as a table node')
    print(50 * '-')
    
if __name__ == '__main__':
    main()