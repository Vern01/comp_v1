def difference(array):
    level = 0
    diff = []
    for first, second in zip(array[0], array[1]):
        diff.append(first - second)
        level += 1
    if len(array[0]) > len(array[1]):
        diff += array[0][level:]
    elif len(array[0]) < len(array[1]):
        diff += array[1][level:]
    return diff
