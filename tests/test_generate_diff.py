import pytest
from gendiff.generate_diff import generate_diff
from test_utils import read_file, get_file_path


@pytest.mark.parametrize('file1_name, file2_name, formatter', [
    ('file1.json', 'file2.json', 'stylish'),
    ('file1.yaml', 'file2.yaml', 'stylish'),
    ('file1.json', 'file2.json', 'plain'),
    ('file1.yaml', 'file2.yaml', 'plain'),
    ('file1.json', 'file2.json', 'json'),
    ('file1.yaml', 'file2.yaml', 'json')
])
def test_generate_diff(file1_name, file2_name, formatter):
    file1 = get_file_path(file1_name)
    file2 = get_file_path(file2_name)
    expect_result = read_file(f"exp_{formatter}.txt")
    actual_result = generate_diff(file1, file2, formatter)

    assert expect_result == actual_result
