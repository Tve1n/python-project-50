import json
import pytest
from gendiff.parser import parse_data_from_file
from test_utils import read_file, get_file_path


@pytest.mark.parametrize('file, result', [
    ('file1.json', 'expect_result_file1.json'),
    ('file1.yaml', 'expect_result_file1.json'),
    ('file2.json', 'expect_result_file2.json'),
    ('file2.yaml', 'expect_result_file2.json')
])
def test_parse_data_from_file(file, result):
    file_path = get_file_path(file)
    expect_result = read_file(result)
    actual_result = parse_data_from_file(file_path)

    assert actual_result == json.loads(expect_result)
