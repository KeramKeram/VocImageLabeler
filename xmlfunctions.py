from xml.etree import ElementTree as et
from pathlib import Path


def get_root(file):
    with open(file, encoding="utf8") as f:
        tree = et.parse(f)
        root = tree.getroot()
        return root, tree
    return None, None


def create_xml(template_xml, folder, filename, width, height, xmin, ymin, xmax, ymax, out_folder, class_name,
               number, ml_path):
    root, tree = get_root(template_xml)
    for elem in root.getiterator():
        try:
            elem.text = elem.text.replace('folder', folder)
            elem.text = elem.text.replace('filename', filename)
            elem.text = elem.text.replace('path', str(ml_path) + "/" + filename)
            elem.text = elem.text.replace('width', str(width))
            elem.text = elem.text.replace('height', str(height))
            elem.text = elem.text.replace('name', class_name)
            elem.text = elem.text.replace('x1', str(xmin))
            elem.text = elem.text.replace('y1', str(ymin))
            elem.text = elem.text.replace('x2', str(xmax))
            elem.text = elem.text.replace('y2', str(ymax))
        except AttributeError:
            print("Error during xml parsing.")
            raise AttributeError

    tree.write(out_folder + "/" + class_name + "_" + str(number) + ".xml")
