
def remove_xml_from_file_list(files_list):
    files = list(files_list)
    list_lenght = len(files_list)
    i = 0
    while i < list_lenght:
        file_split = files_list[i].split(".")
        if (len(file_split) > 0) and (file_split[-1].__eq__("xml")):
            files.remove(files_list[i])
        i += 1
    return files
