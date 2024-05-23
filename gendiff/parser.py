import os
import json
import yaml

def get_format_file(file_path):  # Расширение файла
    _, ext = os.path.splitext(file_path)
    return ext[1:]

def get_content_file(file_path):  # открываем файл для чтения
    with open(file_path, 'r') as file:
        return file.read()  # Непонятный момент, зачем читаем

def parse_data(content, format):
    if format == 'json':
        return json.loads(content)
    if format in ['yaml', 'yml']:
        return yaml.safe_load(content)

def parse_data_from_file(file_path):
    content = get_content_file(file_path)
    format = get_format_file(file_path)
    return parse_data(content, format)