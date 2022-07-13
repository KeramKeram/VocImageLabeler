#!/usr/bin/env python
# encoding: utf-8

import npyscreen


class TestApp(npyscreen.NPSApp):
    def main(self):
        main_screen = npyscreen.Form(name="VocImageLabeler", )
        path_to_images_label = main_screen.add(npyscreen.TitleFixedText, name="Path to images:")
        path_to_images = main_screen.add(npyscreen.Textfield, value="type here")
        path_to_labels_label = main_screen.add(npyscreen.TitleFixedText, name="Path to labels:")
        path_to_labels = main_screen.add(npyscreen.Textfield, value="type here")
        path_to_model_label = main_screen.add(npyscreen.TitleFixedText, name="Path to labels:")
        path_to_model = main_screen.add(npyscreen.Textfield, value="type here")
        path_to_images_label = main_screen.add(npyscreen.TitleFixedText, name="To start click button")
        start_button = main_screen.add(npyscreen.Button, name="Start", value_changed_callback=self.start)
        # This lets the user interact with the Form.
        main_screen.edit()

    def start(self, widget):
        pass


if __name__ == "__main__":
    App = TestApp()
    App.run()
