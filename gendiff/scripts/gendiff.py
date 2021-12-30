#!/usr/bin/env python3
import json

from gendiff.cli import get_args


def read_file(filepath):
    with open(filepath) as file:
        return dict(json.load(file))


def generate_diff(first_file, second_file):
    data_first_file = read_file(first_file)
    data_second_file = read_file(second_file)

    keys = sorted(set(data_first_file) | set(data_second_file))

    result = []

    for key in keys:
        first_value = data_first_file.get(key)
        second_value = data_second_file.get(key)

        if first_value is None:
            result.append('+ {0}: {1}'.format(key, second_value))
        elif second_value is None:
            result.append('- {0}: {1}'.format(key, first_value))
        elif first_value == second_value:
            result.append('  {0}: {1}'.format(key, first_value))
        else:
            result.append('- {0}: {1}'.format(key, first_value))
            result.append('+ {0}: {1}'.format(key, second_value))

    return '{{\n  {0}\n}}'.format('\n  '.join(result))


def main():
    args = get_args()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
