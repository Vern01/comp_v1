import remover as r
import re


def equation(string):
    string = string.replace(" X^0", "1")
    string = string.replace("-X^0", "-1")
    return r.string_remover(string, [" ", "*", "X^0", "^1"])
