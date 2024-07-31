import os


FIXTURE_DIR = os.path.join('tests', 'fixtures')


def get_file_path(file):
    return os.path.join(FIXTURE_DIR, file)


def read_file(file_name):
    fixture_path = os.path.join(FIXTURE_DIR, f'{file_name}')
    with open(fixture_path, 'r') as file:
        return file.read()
