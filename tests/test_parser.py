import pytest
import os
from gendiff.parser import parse_data_from_file


FIXTURE_DIR = os.path.join('tests', 'fixtures')


def get_file_path(file):
    return os.path.join(FIXTURE_DIR, file)

@pytest.mark.parametrize('file, file content', [
    ('file1.json', 'file1.txt'),
    ('file1.yaml', 'file1.txt'),
    ('file2.json', 'file2.txt'),
    ('file2.yaml', 'file2.txt')
])
def test_parse_data_from_file(file, file_content):
    file_path = get_file_path(file)
    file_content_path = get_file_path(file_content)
    with open(file_content_path, 'r') as out_res:
        assert parse_data_from_file(file_path) == out_res.read()
