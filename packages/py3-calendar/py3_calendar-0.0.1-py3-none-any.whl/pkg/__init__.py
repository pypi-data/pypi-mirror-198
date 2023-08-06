import datetime as dt
import time



def gregorian_to_hijri(val, printOut: bool):
    if printOut:
        result = (val - 622) * 1.03

        print(result)

        return result
    
    else:
        result = (val - 622) * 1.03
        return result  

def hijri():
    today = dt.date.today()
    year = today.year

    result = (year - 622) * 1.03 + 1

    return round(result)

def gregorian():
    today = dt.date.today()

    year = today.year

    return year

def hijri_to_gregorian(val, PrintOut: bool):
    year = val

    if PrintOut:
        result = round(year * 0.97 + 622)
        print(result)
        return result
    else:
        return round(result)

def timenow():
    now_ = dt.datetime.now()

    return now_

def gregorian_to_buddhist(val, PrintOut: bool):

    result = val + 543

    if PrintOut:
        print(result)
        return result
    else:
        return round(result)


def buddhist_to_gregorian(val, PrintOut: bool):

    result = val - 543

    if PrintOut:
        print(result)
        return result
    else:
        return round(result)



