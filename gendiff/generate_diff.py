from gendiff.parser import parse_data_from_file
from gendiff.generator import generate
from gendiff.formatters.stylish import format_diff_stylish

def generate_diff(file1, file2, formatter='stylish'):
    obj_f1 = parse_data_from_file(file1)
    obj_f2 = parse_data_from_file(file2)
    diff = generate(obj_f1, obj_f2)
    return format_diff_stylish(diff)

#print(generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json'))
