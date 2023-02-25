class DataTypeError(Exception):
    pass


def findUselessNum(list):
    lenList = 0
    _max = list[lenList]
    for i in list:
        raiseCheck(i)
        if _max < i:
            _max = i
        lenList += 1
    return _max / lenList


def raiseCheck(i):
    if type(i) not in [int, float]:
        raise DataTypeError(
            "Invalid data type, must be int or float. You have '{0}' with the type of {1}".format(i, type(i)))


def main():
    try:
        print(findUselessNum([1, 2, 3, 4, 3]))
    except DataTypeError as dtError:
        print("[Except] {0}".format(dtError))


pass

if __name__ == "__main__":
    main()
