import json


def load_json(path):
    f = open(path)
    data = json.load(f)
    f.close()
    return data


def add_rect_to_json(coordinates, class_name, json_data):
    data = {"name": str(class_name),
                        "pose": "Unspecified",
                        "truncated": 0,
                        "difficult": 0,
                        "bndbox": {"xmin": coordinates.x1, "ymin": coordinates.y1, "xmax": coordinates.x2,
                                   "ymax": coordinates.y2}}
    current_data = json_data['data'][0]['annotation']
    if 'object' not in current_data:
        current_data['object'] = []
    current_data['object'].append(data)

    json_data['data'][0]['annotation'] = current_data
    return json_data
