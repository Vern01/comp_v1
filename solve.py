import cmath


def first_degree(array):
    if array[1] == 0:
        print("This first degree is not solvable")
    elif array[0] == 0:
        print("0")
    else:
        array[0] *= -1
        print(str(array[0] / array[1]))


def __quadratic_formula(array):
    d = (array[1]**2) - (4 * array[2] * array[0])
    if d < 0:
        print("This quadratic equation is unsolvable.")
        return None, None
    elif d == 0:
        return (-array[1] - cmath.sqrt(d)) / (2 * array[2]), None
    a2 = (2 * array[2])
    return (-array[1] - cmath.sqrt(d)) / a2, (-array[1] + cmath.sqrt(d)) / a2


def second_degree(array):
    ans1, ans2 = __quadratic_formula(array)
    if ans1 is not None:
        print(ans1.real)
        if ans2 is not None:
            print(ans2.real)
