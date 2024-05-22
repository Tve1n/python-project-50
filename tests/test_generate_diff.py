import pytest
import os
from gendiff.generate_diff import generate_diff


FIXTURE_DIR = os.path.join('tests', 'fixtures')


def get_file_path(file):
    return os.path.join(FIXTURE_DIR, file)


@pytest.mark.parametrize('file1_name, file2_name, result', [
    ('gendiff/file1.json', 'gendiff/file2.json', 'result_generate_diff')
])
def test_generate_diff(file1_name, file2_name, result):
    path = get_file_path(result)
    with open(path, 'r') as out_res:
        assert generate_diff(file1_name, file2_name) == out_res.read()
