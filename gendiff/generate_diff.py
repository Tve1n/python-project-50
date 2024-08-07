from gendiff.parser import parse_data_from_file
from gendiff.generator import generate
from gendiff.formatters.__init__ import format_diff


def generate_diff(file1, file2, formatter='stylish'):
    obj_f1 = parse_data_from_file(file1)
    obj_f2 = parse_data_from_file(file2)
    diff = generate(obj_f1, obj_f2)
    return format_diff(diff, formatter)
