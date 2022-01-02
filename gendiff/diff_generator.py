from os.path import splitext

from gendiff.difference import create_diff
from gendiff.loaders import get_loader


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


def generate_diff(first_file, second_file):
    first_dict = get_data(first_file)
    second_dict = get_data(second_file)

    return create_diff(first_dict, second_dict)
