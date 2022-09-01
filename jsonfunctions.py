from commondatajson import CommonJsonData
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


def prepare_json_file(commn_data):
    json_file_template = open('testtemplatejson.json')
    data_template = json.load(json_file_template)
    current_data = data_template['data'][0]['annotation']
    current_data['folder'] = str(commn_data.folder)
    current_data['filename'] = str(commn_data.filename)
    current_data['path'] = str(str(commn_data.path) + "/" + commn_data.filename)
    current_data['size']['width'] = commn_data.width
    current_data['size']['height'] = commn_data.height
    data_template['data'][0]['annotation'] = current_data
    return data_template
