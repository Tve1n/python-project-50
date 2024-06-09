import json
import pytest
import os
from gendiff.parser import parse_data_from_file


FIXTURE_DIR = os.path.join('tests', 'fixtures')


def get_file_path(file):
    return os.path.join(FIXTURE_DIR, file)

@pytest.mark.parametrize('file, expect_result', [
    ('file1.json', 'expect_result_file1.json'),
    ('file1.yaml', 'expect_result_file1.json'),
    ('file2.json', 'expect_result_file2.json'),
    ('file2.yaml', 'expect_result_file2.json')
])
def test_parse_data_from_file(file, expect_result):
    file_path = get_file_path(file)
    result_path = get_file_path(expect_result)
    with open(result_path, 'r') as result:
        assert parse_data_from_file(file_path) == json.loads(result.read())
