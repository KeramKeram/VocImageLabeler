#!/usr/bin/env python
# encoding: utf-8
from collections import namedtuple
from os import listdir
from os.path import isfile, join
#import detectorjetson
#import jetson.utils


def main():
    paths_tuple = namedtuple('paths', ['path_to_images', 'path_to_images_label', 'path_to_model'])
    paths_tuple.path_to_images = input("Path to images:")
    paths_tuple.path_to_images_label = input("Path to labels:")
    paths_tuple.path_to_model = input("Path to model:")


def start(widget):
    contents = listdir(str(self.path_to_images.value))
    files = filter(lambda f: isfile(join(self.path_to_images.value, f)), contents)
    files_list = list(files)
    detector = detectorjetson.DetectorJetson(32, 32, str(self.path_to_model.value),
                                             str(self.path_to_model_label.value))
    for file in files_list:
        image = jetson.utils.loadImage(str(self.path_to_images_label.value) + "/" + file)
        rect_list = detector.run(image)

if __name__ == "__main__":
    main()
