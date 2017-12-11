def reduced(array):
    if len(array) == 0:
        return ""
    if array[0] == int(array[0]):
        array[0] = int(array[0])
    display = "Reduced form: " + str(array[0])
    index = 1
    for value in array[1:]:
        if value > -1:
            display += " + "
        else:
            display += " - "
        if int(value) == value:
            value = int(value)
        display += str(abs(value)) + "X^" + str(index)
        index += 1
    display += " = 0"
    return display
