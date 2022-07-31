#!/usr/bin/env python
# encoding: utf-8
import detectorjetson
from os import listdir
from os.path import isfile, join
import jetson.utils
import npyscreen


class TestApp(npyscreen.NPSApp):
    def __init__(self):
        self.path_to_model = None
        self.path_to_model_label = None
        self.path_to_labels = None
        self.path_to_labels_label = None
        self.path_to_images = None
        self.path_to_images_label = None

    def main(self):
        main_screen = npyscreen.Form(name="VocImageLabeler", )
        self.path_to_images_label = main_screen.add(npyscreen.TitleFixedText, name="Path to images:")
        self.path_to_images = main_screen.add(npyscreen.Textfield, value="type here")
        self.path_to_labels_label = main_screen.add(npyscreen.TitleFixedText, name="Path to labels:")
        self.path_to_labels = main_screen.add(npyscreen.Textfield, value="type here")
        self.path_to_model_label = main_screen.add(npyscreen.TitleFixedText, name="Path to model:")
        self.path_to_model = main_screen.add(npyscreen.Textfield, value="type here")
        self.path_to_images_label = main_screen.add(npyscreen.TitleFixedText, name="To start click button")
        start_button = main_screen.add(npyscreen.Button, name="Start", value_changed_callback=self.start)
        # This lets the user interact with the Form.
        main_screen.edit()

    def start(self, widget):
        contents = listdir(str(self.path_to_images.value))
        files = filter(lambda f: isfile(join(self.path_to_images.value,f)),contents)
        files_list = list(files)
        detector = detectorjetson.DetectorJetson(32, 32, str(self.path_to_model.value),
                                                 str(self.path_to_model_label.value))
        for file in files_list:
            image = jetson.utils.loadImage(str(self.path_to_images_label.value) + "/" + file)
            rect_list = detector.run(image)

if __name__ == "__main__":
    App = TestApp()
    App.run()
