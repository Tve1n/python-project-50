import os
import pytest
from gendiff.generate_diff import generate_diff


FIXTURE_DIR = os.path.join('tests', 'fixtures')


def get_file_path(file):
    return os.path.join(FIXTURE_DIR, file)


def read_file(file_name):
    fixture_path = os.path.join(FIXTURE_DIR, f'{file_name}')
    with open(fixture_path, 'r') as file:
        return file.read()


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
