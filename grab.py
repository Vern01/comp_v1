import find


def backward(string, index):
    if index == -1:
        index = len(string)
    start = 0
    if string[0] == '-':
        start = 1
    return string[start:index]


def forward(string, index):
    index += 1
    next_index, o_type = find.operators(string, index)
    if next_index == -1:
        return string[index:]
    return string[index:next_index]
