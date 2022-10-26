#!/usr/bin/env python
# encoding: utf-8
from Json2PascalVoc.Converter import Converter
from collections import namedtuple
from commondatajson import CommonJsonData
from os import listdir
from os.path import isfile, join
import filtring
import json
import jsonfunctions
from strategy import Context


def main():
    paths_tuple = namedtuple('ui', ['type', 'path_to_images', 'path_to_images_label', 'path_to_model'])
    print("Choose type of device. \n 1. Jetson nano(dusty) \n 2. Pc by pytroch-ssd \n")
    paths_tuple.type = input("Type 1 or 2:")
    paths_tuple.path_to_images = input("Path to images:")
    paths_tuple.path_to_images_label = input("Path to labels:")
    paths_tuple.path_to_model = input("Path to model:")
    start(paths_tuple)


def start(paths_tuple):
    contents = listdir(str(paths_tuple.path_to_images))
    files = filter(lambda f: isfile(join(paths_tuple.path_to_images, f)), contents)
    files_list = filtring.remove_xml_from_file_list(list(files))
    ctx = Context(paths_tuple.type)
    json_converter = Converter()
    for file in files_list:
        rect_list, width, height = ctx.execute(file)
        labels_dict = create_labels(paths_tuple.path_to_images_label)
        common_file_data = CommonJsonData(paths_tuple.path_to_images, file,
                                          str(paths_tuple.path_to_images) + "/" + file, width, height)
        json_file = jsonfunctions.prepare_json_file(common_file_data)
        create_voc_files(rect_list, labels_dict, json_converter, json_file)


def create_labels(path_to_images_label):
    labels_dict = dict()
    labels_counter = 0
    lines = None
    with open(str(path_to_images_label), 'r') as f:
        lines = f.readlines()
    for line in lines:
        labels_dict[str(labels_counter)] = str(line)
        labels_counter = labels_counter + 1
    return labels_dict


def create_voc_files(rect_list, labels_dict, json_converter, json_file):
    for key in rect_list:
        for value in rect_list[key]:
            json_file = jsonfunctions.add_rect_to_json(value[1], value[2], value[3], value[4],
                                                       labels_dict[str(value[0])], json_file)
        json_object = json.dumps(json_file, indent=4)
        with open("translationfile.json", "w") as outfile:
            outfile.write(json_object)
        json_converter.convertJsonToPascal("translationfile.json")


if __name__ == "__main__":
    main()
