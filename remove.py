def string(full_string, removables):
    for remove in removables:
        full_string = full_string.replace(remove, "")
    return full_string


def array_redundant(array):
    while array[-1] == 0:
        del array[-1]
    return array
