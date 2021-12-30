from gendiff.scripts.gendiff import generate_diff


def test_generate_diff():
    file1 = 'gendiff/tests/fixtures/file1.json'
    file2 = 'gendiff/tests/fixtures/file2.json'

    with open('gendiff/tests/fixtures/result', 'r') as file:
        expected_data = file.read()

    assert generate_diff(file1, file2) == expected_data
