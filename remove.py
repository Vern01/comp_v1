def string(full_string, removables):
    for remove in removables:
        full_string = full_string.replace(remove, "")
    return full_string
