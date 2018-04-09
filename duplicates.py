import argparse
import os
from collections import defaultdict


def walk_directory(filepath):
    files_dict = defaultdict(list)
    for dirpath, dirnames, filenames in os.walk(filepath):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_size = os.path.getsize(file_path)
            filename_index = '{}{}'.format(filename, file_size)
            files_dict[filename_index].append(file_path)
    return files_dict


def find_file_duplicates(files_dict):
    duplicates = defaultdict(list)
    for file, pathes in files_dict.items():
        if len(pathes) >= 2:
            duplicates[file] = pathes
    return duplicates


def get_args():
    parser = argparse.ArgumentParser(
        description='Recursively find duplicate files on specific path'
    )
    parser.add_argument(
        '-f', '--filepath',
        help='target folder to find duplicates into',
        required=True
    )
    return parser.parse_args()


if __name__ == '__main__':

    args = get_args()

    files = walk_directory(args.filepath)

    file_duplicates = find_file_duplicates(files)

    if file_duplicates:
        print('We have found next duplicates in the folder: {folder}'
              .format(folder=args.filepath))
        for duplicate in file_duplicates.values():
            print('\n'.join(duplicate))
    else:
        print('There are no duplicates in the folder {folder}'
              .format(folder=args.filepath))
