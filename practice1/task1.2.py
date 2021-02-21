import math

def f12(x):
    res = 0
    if (x < 74):
        res = (math.tan(94*(math.pow(x,7))) + math.pow(x,3))
    elif (x < 153):
        res = (math.pow(x,3) + math.pow(x,7)/99)
    elif (x < 203):
        res = (54 * math.pow(x,7) + math.sin(x))
    elif (x < 295):
        res = 77* math.pow((math.pow(x,5)-math.sin(x)),2) - x
    else:
        res = math.exp(math.pow(x,3) + 84*x) - math.cos(x) + 27
    return res
#print(f12(167))