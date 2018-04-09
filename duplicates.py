import argparse
import os
from itertools import groupby


def get_args():
    parser = argparse.ArgumentParser(
        description='Recursively find duplicate '
                    'files on specific path'
    )
    parser.add_argument(
        '-p', '--filepath',
        help='target folder to find duplicates into',
        required=True
    )
    return parser.parse_args()


def walk_directory(filepath):
    for dirpath, dirnames, filenames in os.walk(filepath):
        for filename in filenames:
            yield dirpath, filename


def calc_file_sizes(filepaths):
    for filepath in filepaths:
        dirpath, filename = filepath
        file_path = os.path.join(dirpath, filename)
        file_size = os.path.getsize(file_path)
        yield dirpath, filename, file_size


def get_duplicate_files(filepaths_with_sizes):
    sorted_files = sorted(
        filepaths_with_sizes,
        key=lambda file: file[1] + str(file[2])
    )
    grouped_files = groupby(
        sorted_files,
        key=lambda file: file[1] + str(file[2])
    )
    for _, group in grouped_files:
        current_group = list(group)
        if len(current_group) >= 2:
            yield from current_group


if __name__ == '__main__':

    args = get_args()

    files_in_directory = walk_directory(args.filepath)

    files_with_sizes = list(calc_file_sizes(files_in_directory))

    duplicates = list(get_duplicate_files(files_with_sizes))

    if duplicates:
        print('We have found next duplicates '
              'in the folder: {folder}'.format(folder=args.filepath))
        for duplicate in duplicates:
            print(os.path.join(duplicate[0], duplicate[1]))
    else:
        print('There are no duplicates '
              'in the folder {folder}'.format(folder=args.filepath))
