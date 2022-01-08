from os.path import splitext

from gendiff.diff_builder import build_diff
from gendiff.loaders import get_loader
from gendiff.stylish import stylish


def read_file(filepath):
    with open(filepath) as file:
        return file.read()


def get_data(filepath):
    _, ext = splitext(filepath)
    load = get_loader(ext[1:])
    if load:
        data = read_file(filepath)
        return load(data)
    raise ValueError


def generate_diff(first_file, second_file, formatter=stylish):
    first_dict = get_data(first_file)
    second_dict = get_data(second_file)

    diff = build_diff(first_dict, second_dict)

    return formatter(diff)
