import os
import json
import yaml


def get_format_file(file_path):  # Расширение файла
    _, ext = os.path.splitext(file_path)
    return ext[1:]


def parse_data(content, format):
    if format == 'json':
        return json.load(content)
    if format in ['yaml', 'yml']:
        return yaml.safe_load(content)
    raise ValueError(f"Unsupported file format: {format}")


def parse_data_from_file(file_path):
    content = open(file_path, 'r')
    format = get_format_file(file_path)
    return parse_data(content, format)
