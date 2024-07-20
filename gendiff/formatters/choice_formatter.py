from gendiff.formatters.stylish import format_diff_stylish

def format_diff(diff, formatter):
    if formatter == 'stylish':
        return format_diff_stylish(diff)