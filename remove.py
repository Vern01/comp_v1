import re


def whitespace(string):
    return re.sub("[\s]", "", string)


def string(full_string, removables):
    full_string = whitespace(full_string)
    for remove in removables:
        full_string = full_string.replace(remove, "")
    return full_string


def array_redundant(array):
    while len(array) > 1 and array[-1] == 0:
        del array[-1]
    return array
