import purify
import find


def backward_grab(string, index):
    start = 0
    if string[0] == '-':
        start = 1
    return string[start:index]


def forward_grab(string, index):
    index += 1
    next_index, o_type = find.operators(string, index)
    if next_index == -1:
        return string[index:]
    return string[index:next_index]


def check_array_order(array, level):
    while level > len(array) - 1:
        array.append([0])


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
    print(string)
    if string.isalpha():
        check_array_order(array, 1)
        array[1].append(1.0 * o_type)
    else:
        value, level = value_level_read(string)
        check_array_order(array, level)
        array[level].append(value * o_type)


def main():
    test = "-3X^0 + X^0 + 2X^1 + 5X^2"
    array = [[0]]
    pure_string = purify.equation(test)
    index, o_type = find.operators(pure_string, 0)
    if index != 0:
        build_2d_array(array, backward_grab(pure_string, index), 1)
    else:
        build_2d_array(array, forward_grab(pure_string, index), -1)
        index += 1
    while 42:
        index, o_type = find.operators(pure_string, index)
        if index == -1:
            break
        build_2d_array(array, forward_grab(pure_string, index), o_type)
        index += 1
    print(array)


if __name__ == '__main__':
    main()
