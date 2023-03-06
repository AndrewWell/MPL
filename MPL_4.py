import re as regex


class VolumeError(Exception):
    pass


class DataTypeError(Exception):
    pass


def raiseCheck(_string: str, maxValue: int):
    if (_type := type(_string)) not in [str]:
        raise DataTypeError("Invalid data type. You have '{0}' with the type of {1}".format(_string, _type))
    elif (_len := len(_string)) > maxValue:
        raise VolumeError(
            "Line size exceeded. It`s possible to use {0} characters, you have {1}".format(maxValue, _len))
    return True


def validityCheck():
    pass


def removeMultipleChar(string: str) -> str:
    raiseCheck(string, 40)
    newString = [None]
    for i in string.upper():
        if i != newString[-1]:
            newString.append(i)
    return ''.join(newString[1:])


def checkCharOneByOne(string: str, searchSymbol: chr) -> bool:
    num = 0
    for i in string:
        if i == searchSymbol:
            num += 1
            if num > 1: return False
        else:
            num = 0
    return True


def checkCorrectEmail(email: str) -> bool:
    splitEmail = email.split("@")

    if len(splitEmail) > 2: return False
    if not checkCharOneByOne(email, "."): return False
    if len(splitEmail[0]) > 64: return False

    pattern = regex.compile(r'([A-Za-z0-9]+[.-_+])*[A-Za-z0-9]+@([A-Za-z0-9]+[.-_+])*[A-Za-z0-9]+(\.[A-Z|a-z]{2,255})+')
    return True if regex.fullmatch(pattern, email) else False


def findEmails(text: str) -> bool or list:
    raiseCheck(text, 320)
    wordList = text.split()
    possibleEmails = []
    for i in wordList:
        if "@" in i:
            if checkCorrectEmail(i):
                possibleEmails.append(i)
    return possibleEmails if len(possibleEmails) != 0 else False


def main():
    try:
        # print(removeMultipleChar("HEEELLLLO WOOOrRRRDdD"))

         if not (allEmail := findEmails("foo@ya.ru foo.@ya.ru foo@.ya.ru -foo@ya.ru .foo@ya.ru")):
            print("Email addresses not found")
         else:
            print(f"Found the following email addresses: {allEmail}")

    except VolumeError as vError:
        print(f"[Except]: {vError}")
    except DataTypeError as dtError:
        print(f"[Except]: {dtError}")
    pass


if __name__ == "__main__":
    main()
