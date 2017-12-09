import remove


def equation(string):
    string = string.replace(" X^0", "1")
    string = string.replace("-X^0", "-1")
    return remove.string(string, [" ", "*", "X^0", "^1"])


def array2D(array):
    return [sum(lst) for lst in array]
