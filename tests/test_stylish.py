import pytest
from gendiff.formatters.stylish import to_str, make_stylish_result
from test_utils import get_input_data, get_expected_result


@pytest.mark.parametrize('input_value, expected_value', [
    (None, 'null'),
    (False, 'false'),
    ('string', 'string'),
    (2000, '2000'),
    (1000.7, '1000.7')
])
def test_to_str(input_value, expected_value):
    assert to_str(input_value) == expected_value


def test_make_stylish_result():
    input = get_input_data('input_diff.json')
    expected = get_expected_result('exp_stylish.txt')
    assert make_stylish_result(input) == expected
