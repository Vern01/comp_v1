#!/usr/bin/env python3
import sys

import display
import find
import grab
import merge
import purify
import remove
import solve


def check_array_order(array, level):
    while level > len(array) - 1:
        array.append([])


def value_level_read(string):
    if string.isdigit():
        return float(string), 0
    elif string.find('^') == -1:
        return float(string[:find.first_alpha(string)]), 1
    else:
        end = find.first_alpha(string)
        if end == 0:
            value = 1.0
        else:
            value = float(string[:end])
        return value, int(string[string.index('^') + 1:])


def build_2d_array(array, string, o_type):
    if string.isalpha():
        check_array_order(array, 1)
        array[1].append(1.0 * o_type)
    else:
        value, level = value_level_read(string)
        check_array_order(array, level)
        array[level].append(value * o_type)


def simplify(equation):
    array = [[]]
    index, o_type = find.operators(equation, 0)
    if index != 0 or index == -1:
        build_2d_array(array, grab.backward(equation, index), 1)
    else:
        build_2d_array(array, grab.forward(equation, index), -1)
        index += 1
    while 42:
        index, o_type = find.operators(equation, index)
        if index == -1:
            break
        build_2d_array(array, grab.forward(equation, index), o_type)
        index += 1
    return purify.array2d(array)


def main():
    # try:
        equations = purify.equation(sys.argv[1]).split('=')
        a = merge.difference([simplify(eq) for eq in equations])
        a = remove.array_redundant(a)
        print(display.reduced(a))
        print("Polynomial degree: " + str(len(a) - 1))
        if len(a) == 1:
            if a[0] == 0:
                print("All real numbers are a solution.")
            else:
                print("This equation is not possible.")
        elif len(a) == 2:
            solve.first_degree(a)
        elif len(a) == 3:
            solve.second_degree(a)
        else:
            print("I cannot solve the polynomial degree of " + str(len(a) - 1))
    # except Exception:
    #     print("The format of your input is incorrect. Here are a few tips:\n"
    #           "\tUse quotation marks around your equation. i.e ./computerV1.py \"42X + 42 = 0\"\n"
    #           "\tUse the '^' sign to indicate the power of the value X\n"
    #           "\tMake sure there is a '=' that is either set to 0 or equation of your choice.\n"
    #           "\tMake sure to remove anything that is not necessary to solve the equation.")


if __name__ == '__main__':
    main()
