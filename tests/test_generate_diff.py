from gendiff.scripts.gendiff import generate_diff

import pytest

@pytest.mark.parametrize("file1,file2,expected_file", [(
    'tests/fixtures/file1.json',
    'tests/fixtures/file2.json',
    'tests/fixtures/result',
), (
    'tests/fixtures/file1.yml',
    'tests/fixtures/file2.yml',
    'tests/fixtures/result',
),
(
    'tests/fixtures/file1.yaml',
    'tests/fixtures/file2.yaml',
    'tests/fixtures/result',
)])

def test_generate_diff(file1, file2, expected_file):
    with open(expected_file, 'r') as file:
        expected_data = file.read()

    assert generate_diff(file1, file2) == expected_data
