from gendiff.scripts.gendiff import generate_diff

import pytest

@pytest.mark.parametrize("file1,file2,expected_file", [(
    'tests/fixtures/plain/file1.json',
    'tests/fixtures/plain/file2.json',
    'tests/fixtures/plain/result',
), (
    'tests/fixtures/plain/file1.yml',
    'tests/fixtures/plain/file2.yml',
    'tests/fixtures/plain/result',
), (
    'tests/fixtures/plain/file1.yaml',
    'tests/fixtures/plain/file2.yaml',
    'tests/fixtures/plain/result',
), (
    'tests/fixtures/nested/file1.json',
    'tests/fixtures/nested/file2.json',
    'tests/fixtures/nested/result',
), (
    'tests/fixtures/nested/file1.yml',
    'tests/fixtures/nested/file2.yml',
    'tests/fixtures/nested/result',
)])

def test_generate_diff(file1, file2, expected_file):
    with open(expected_file, 'r') as file:
        expected_data = file.read()

    assert generate_diff(file1, file2) == expected_data
