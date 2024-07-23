from gendiff.formatters.stylish import format_diff_stylish
from gendiff.formatters.plain import format_diff_plain
from gendiff.formatters.json import format_diff_json


def format_diff(diff, formatter):
    if formatter == 'stylish':
        return format_diff_stylish(diff)
    if formatter == 'plain':
        return format_diff_plain(diff)
    if formatter == 'json':
        return format_diff_json(diff)
