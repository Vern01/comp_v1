import remove


def equation(string):
    return remove.string(string, [" ", "*"])


def array2d(array):
    return [sum(lst) for lst in array]
