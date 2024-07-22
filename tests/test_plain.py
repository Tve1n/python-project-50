import pytest
from gendiff.formatters.plain import to_str, format_diff_plain
from test_utils import get_input_data, get_expected_result


@pytest.mark.parametrize('input_value, expected_value', [
    ('I am string', '"I am string"'),
    (True, 'true'),
    (20000, '20000'),
    (1000.7, '1000.7'),
    ([1, 2, 3], '[complex value]'),
    ([1, [2, [3, 4]]], '[complex value]'),
    ({'key': {'key23': 'value'}}, '[complex value]'),
    ({'key': 'value'}, '[complex value]'),
    ([], '[complex value]'),
    ({}, '[complex value]'),
    (None, 'null')

])
def test_to_str(input_value, expected_value):
    assert to_str(input_value) == expected_value


def test_format_diff_plain():
    input = get_input_data('input_diff.json')
    expected = get_expected_result('exp_plain.txt')
    assert format_diff_plain(input) == expected
