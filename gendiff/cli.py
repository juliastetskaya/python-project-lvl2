import argparse


def get_parser():
    parser = argparse.ArgumentParser(description='Generate diff')

    parser.add_argument('first_file')
    parser.add_argument('second_file')

    return parser


def get_args():
    parser = get_parser()

    return parser.parse_args()
