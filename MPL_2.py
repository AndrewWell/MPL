import math


class DataTypeError(Exception):
    pass


def raiseCheck(i):
    if type(i) not in [int, float]:
        raise DataTypeError(
            "Invalid data type, must be int or float. You have '{0}' with the type of {1}".format(i, type(i)))


def func(k, x, d, n, b, c):
    raiseCheck(k)
    raiseCheck(x)
    raiseCheck(d)
    raiseCheck(n)
    raiseCheck(b)
    raiseCheck(c)

    degree = d ** n
    root = math.sqrt(c)
    fractions = math.cos(k * x) / math.sin(0.3)
    return round(-fractions + degree * b * root, 3)


def main():
    try:
        print(func(2, 0.32, 1.25, -4, 0.75, 2.2))
    except DataTypeError as dtError:
        print("[Except] {0}".format(dtError))


pass

if __name__ == "__main__":
    main()
