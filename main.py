#!/usr/bin/env python
# encoding: utf-8
from collections import namedtuple
from os import listdir
from os.path import isfile, join
import detectorjetson
import jetson.utils


def main():
    paths_tuple = namedtuple('paths', ['path_to_images', 'path_to_images_label', 'path_to_model'])
    paths_tuple.path_to_images = input("Path to images:")
    paths_tuple.path_to_images_label = input("Path to labels:")
    paths_tuple.path_to_model = input("Path to model:")
    start(paths_tuple)


def start(paths_tuple):
    contents = listdir(str(paths_tuple.path_to_images))
    files = filter(lambda f: isfile(join(paths_tuple.path_to_images, f)), contents)
    files_list = list(files)
    detector = detectorjetson.DetectorJetson(32, 32, str(paths_tuple.path_to_model),
                                             str(paths_tuple.path_to_images_label))
    for file in files_list:
        image = jetson.utils.loadImage(str(paths_tuple.path_to_images) + "/" + file)
        rect_list = detector.run(image)


if __name__ == "__main__":
    main()
