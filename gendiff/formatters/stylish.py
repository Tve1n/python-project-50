import itertools


SEPARATOR = " "
ADD = '+ '
DELETE = '- '
NONE = '  '


def get_indent(depth):
    return SEPARATOR * (depth * 4 - 2)


def to_str(value, depth):
    if value is None:
        return "null"
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, dict):
        indent = get_indent(depth + 1)
        lines = []
        for key, inner_value in value.items():
            formated_value = to_str(inner_value, depth + 1)
            lines.append(f"{indent}{NONE}{key}: {formated_value}")

        end_ident = '' if depth == 0 else "  "
        result = itertools.chain(
            "{", lines, [get_indent(depth) + end_ident + "}"]
        )
        return '\n'.join(result)
    return f"{value}"


def make_stylish_result(diff, depth=0):  # noqa: C901
    indent = get_indent(depth + 1)
    lines = []
    for item in diff:
        key_name = item['name']
        old_value = to_str(item.get("old_value"), depth + 1)
        new_value = to_str(item.get("new_value"), depth + 1)
        action = item['action']
        if action == "unchanged":
            current_value = to_str(item.get('value'), depth)
            lines.append(f"{indent}{NONE}{key_name}: {current_value}")
        elif action == "modified":
            lines.append(f"{indent}{DELETE}{key_name}: {old_value}")
            lines.append(f"{indent}{ADD}{key_name}: {new_value}")
        elif action == 'deleted':
            lines.append(f"{indent}{DELETE}{key_name}: {old_value}")
        elif action == 'added':
            lines.append(f"{indent}{ADD}{key_name}: {new_value}")
        elif action == 'nested':
            children = make_stylish_result(
                item.get("children"), depth + 1
            )
            lines.append(f"{indent}{NONE}{key_name}: {children}")

    end_ident = '' if depth == 0 else "  "
    result = itertools.chain(
        "{", lines, [get_indent(depth) + end_ident + "}"]
    )

    return '\n'.join(result)


def format_diff_stylish(data):
    return make_stylish_result(data)
