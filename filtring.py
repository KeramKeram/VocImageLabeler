
def remove_xml_from_file_list(files_list):
    for image_file in files_list:
        file_split = image_file.split(".")
        if (len(file_split) > 0) and (file_split[-1].__eq__("xml")):
            files_list.remove(image_file)
    return files_list
