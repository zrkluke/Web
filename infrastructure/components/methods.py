import json
from collections import namedtuple


def convert_to_json(data):
    return json.dumps(data)


def convert_from_json(data):
    return json.loads(data)
