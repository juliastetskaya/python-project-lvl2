from gendiff.scripts.gendiff import generate_diff


def test_generate_diff():
    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file2.json'

    with open('tests/fixtures/result', 'r') as file:
        expected_data = file.read()

    assert generate_diff(file1, file2) == expected_data
