import pytest
import os
from gendiff.generate_diff import generate_diff


FIXTURE_DIR = os.path.join('tests', 'fixtures')


def get_file_path(file):
    return os.path.join(FIXTURE_DIR, file)


@pytest.mark.parametrize('file1_name, file2_name, result', [
    ('file1.json', 'file2.json', 'result_generate_diff'),
    ('file1.yaml', 'file2.yaml', 'result_generate_diff')
])
def test_generate_diff(file1_name, file2_name, result):
    file1 = get_file_path(file1_name)
    file2 = get_file_path(file2_name)
    result_path = get_file_path(result)
    with open(result_path, 'r') as out_res:
        assert generate_diff(file1, file2) == out_res.read()
