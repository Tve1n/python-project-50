import json


def format_diff_json(data):
    return json.dumps(data, indent=4, separators=(',', ': '))
