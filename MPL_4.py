import re as regex
class VolumeError(Exception):
    pass
class DataTypeError(Exception):
    pass

def raiseCheck(_string, maxValue):
    if (_type:= type(_string)) not in [str]:
        raise DataTypeError("Invalid data type. You have '{0}' with the type of {1}".format(_string, _type))
    elif (_len := len(_string)) > maxValue:
        raise VolumeError("Line size exceeded. It`s possible to use {0} characters, you have {1}".format(maxValue,_len))

def removeMultipleChar(string):
    raiseCheck(string,40)
    newString = [None]
    for i in string.upper():
        if i != newString[-1]:
            newString.append(i)
    return ''.join(newString[1:])

def checkCorrectEmail(email):
    #(username)@(domainName).(topLevelDomain)
    return True if regex.fullmatch(r'(A-Za-z0-9]+[.-_])*[A-Za-Za-z0-9-]+[\.[A-Z|a-z]{2,})+') else False

def main():
    try:
        print(removeMultipleChar("HEEELLLLO WOOOrRRRDdD"))
    except VolumeError as vError:
        print(f"[Except]: {vError}")
    except DataTypeError as dtError:
        print(f"[Except]: {dtError}")
    pass

if __name__=="__main__":
    main()
