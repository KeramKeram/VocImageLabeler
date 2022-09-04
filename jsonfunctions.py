from commondatajson import CommonJsonData
import json


def load_json(path):
    f = open(path)
    data = json.load(f)
    f.close()
    return data


def add_rect_to_json(x1,  y1,  x2,  y2, class_name, json_data):
    data = {"name": str(class_name),
            "pose": "Unspecified",
            "truncated": 0,
            "difficult": 0,
            "bndbox": {"xmin": x1, "ymin": y1, "xmax": x2, "ymax": y2}}
    current_data = json_data['data'][0]['annotation']
    if 'object' not in current_data:
        current_data['object'] = []
    current_data['object'].append(data)

    json_data['data'][0]['annotation'] = current_data
    return json_data


def prepare_json_file(commondata):
    json_file_template = open('testtemplatejson.json')
    data_template = json.load(json_file_template)
    current_data = data_template['data'][0]['annotation']
    current_data['folder'] = str(commondata.folder)
    current_data['filename'] = str(commondata.filename)
    current_data['path'] = str(str(commondata.path))
    current_data['size']['width'] = commondata.width
    current_data['size']['height'] = commondata.height
    data_template['data'][0]['annotation'] = current_data
    return data_template
