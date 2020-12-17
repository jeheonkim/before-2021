number = float(input("put down the number including the decimal point."))
def positiveconvert(floatnum):
    converted = str(floatnum)
    x = len(converted)
    firstComp = converted[0]+"."+converted[1,x]
    print(firstComp)
def negativeconvert(floatnum):
    return True
if number > 10:
    print(positiveconvert(number))
elif number == 10:
    print("1 * 10^1")
elif number < 10:
    print(negativeconvert(number))

