import json


def load_json(path):
    f = open(path)
    data = json.load(f)
    f.close()
    return data


def add_rect_to_json(coordinates, class_name, json_data):
    return json_data
