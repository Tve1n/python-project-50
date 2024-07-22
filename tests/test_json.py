from gendiff.formatters.json import format_diff_json
from test_utils import get_input_data, get_expected_result


def test_format_diff_json():
    input = get_input_data('input_diff.json')
    expected = get_expected_result('exp_json.txt')
    assert format_diff_json(input) == expected
