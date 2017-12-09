import re


def operators(full_string, index):
    try:
        index = re.search('[+-]', full_string[index:]).start() + index
        o_type = int(full_string[index] + "1")
    except AttributeError:
        return -1, 1
    return index, o_type


def first_alpha(full_string):
    return re.search('[a-zA-Z]', full_string).start()
