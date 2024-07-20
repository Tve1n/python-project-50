import pytest
from gendiff.generator import(
    generate, for_add, for_delete, for_unchanged, for_modified, for_nested
)


def test_for_add():
    result = for_add('key1', 'value1')
    assert result == {'action': 'added',
                      'name': 'key1',
                      'new_value': 'value1'}


def test_for_delete():
    result = for_delete('key0', 'value0')
    assert result == {'action': 'deleted',
                      'name': 'key0',
                      'new_value': 'key0'}


def test_for_unchanged():
    result = for_unchanged('key2', 'value2')
    assert result == {'action': 'unchanged',
                      'name': 'key2',
                      'value': 'value2'}


def test_for_modified():
    result = for_modified('key3', 'value3_old', 'value3_new')
    assert result == {'action': 'modified',
                      'name': 'key3',
                      'old_value': 'value3_old',
                      'new_value': 'value3_new'}


def test_for_nested():
    old_dict = {'a': 1, 'b': 2}
    new_dict = {'a': 1, 'b': 3, 'c': 4}
    result = for_nested('key4', old_dict, new_dict)
    assert result == {
        'action': 'nested',
        'name': 'key4',
        'children': [
            {'action': 'unchanged', 'name': 'a', 'value': 1},
            {'action': 'modified', 'name': 'b', 'old_value': 2,'new_value': 3},
            {'action': 'added', 'name': 'c', 'new_value': 4}
        ]
    }


@pytest.fixture
def file1():
    return {
        'common': {
            'setting1': 'Value 1',
            'setting2': 200,
            'setting4': 5000

        }
    }


@pytest.fixture
def file2():
    return {
        'common': {
            'setting1': 'Value 1',
            'setting3': None,
            'setting4': 'five thousand'
        }
    }


@pytest.fixture
def expected_result():
    return [
        {
            'action': 'nested',
            'name': 'common',
            'children': [
                {'action': 'unchanged', 'name': 'setting1', 'value': 'Value 1'},
                {'action': 'deleted', 'name': 'setting2', 'old_value': 200},
                {'action': 'added', 'name': 'setting3', 'new_value': None},
                {'action': 'modified', 'name': 'setting4', 'old_value': 5000, 'new_value': 'five thousand'}
            ],
        },
    ]


def test_generate(file1, file2, expected_result):
    result = generate(file1, file2)
    assert result == expected_result