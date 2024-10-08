

def to_str(value):
    if isinstance(value, (list, dict)):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return str(value)


def make_plain_result_item(item, path=''):  # передается элемент словаря
    current_key = item.get('name')
    if path:
        current_path = f"{path}.{current_key}"
    else:
        current_path = current_key
    action = item.get('action')
    new_value = to_str(item.get('new_value'))
    old_value = to_str(item.get('old_value'))

    match action:
        case 'added':
            return (
                f"Property '{current_path}' "
                f"was added with value: {new_value}"
            )
        case 'deleted':
            return f"Property '{current_path}' was removed"
        case 'modified':
            return (
                f"Property '{current_path}' was updated. "
                f"From {old_value} to {new_value}"
            )
        case 'nested':
            children = item.get('children')
            return make_plain_result(children, current_path)
        case 'unchanged':
            return None
        case _:
            raise Exception("Unknown type of action")


def make_plain_result(diff, path=''):
    result = []
    for item in diff:
        formated_item = make_plain_result_item(item, path)
        if formated_item is not None:
            result.append(formated_item)

    return '\n'.join(result)


def format_diff_plain(data):
    return make_plain_result(data)
