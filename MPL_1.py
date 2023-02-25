class Error(Exception):
    pass


class DataTypeError(Error):
    pass


class ValueTooSmallError(Error):
    pass


class ValueTooLargeError(Error):
    pass


def checkingRaise(x_start, x_end, step):
    if x_start > x_end:
        raise ValueTooSmallError("The end value of the interval cannot be greater than the start value")
    elif x_end - x_start < step:
        raise ValueTooLargeError("The change step cannon be greater than the length of the range")


def typeChecking(i):
    if type(i) not in [int, float]:
        raise DataTypeError(
            "Invalid data type, must be int or float. You have '{0}' with the type of {1}".format(i, type(i)))


def func(a, b, c, x):

    if x + 5 < 0 and c == 0:
        return 1 / (a * x) - b
    return (x - a) / x if a + 5 != 0 and c != 0 else 10 * x / (c - 4)


def cyclicFunc(x_start, x_end, step, a, b, c):
    typeChecking(x_start)
    typeChecking(x_end)
    typeChecking(step)
    checkingRaise(x_start, x_end, step)

    x = x_start
    while True:
        result = func(a, b, c, x)
        print("%.2f %3.f %8.2f %3d %3d %3d" % (x, result, step, a, b, c))
        x += step
        if x > x_end:
            break
    pass


def main():
    try:
        x_start = float(input("Enter the initial value if the interval: "))
        x_end = float(input("Enter the end value of the interval: "))
        step = float(input("Enter change step: "))

        a = int(input("Enter the value of variable (a): "))
        b = int(input("Enter the value of variable (b): "))
        c = int(input("Enter the value of variable (c): "))

        print("\n\t=====Start panel=====")
        print("Start value: {0}, end value: {1}, step: {2}\n".format(x_start, x_end, step))
        print("%2s %7s %6s %3s %3s %3s" % ('x', 'F(x)', 'step', 'a', 'b', 'c'))

        cyclicFunc(x_start, x_end, step, a, b, c)

    except ValueError as vError:
        print("[Except]: {0}".format(vError))
    except ValueTooLargeError as vtlError:
        print("[Except]: {0}".format(vtlError))
    except ValueTooSmallError as vtsError:
        print("[Except]: {0}".format(vtsError))
    except ZeroDivisionError as zError:
        print("[Except]: {0}".format(zError))
    except DataTypeError as dtError:
        print("[Except]: {0}".format(dtError))
    pass


if __name__ == "__main__":
    main()
