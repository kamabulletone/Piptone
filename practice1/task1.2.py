import math

def f12():
    x = float(input("x = "))
    if (x < 74):
        return (math.tan(94*(math.pow(x,7))) + math.pow(x,3))
    elif (x < 153 and x >=74):
        return (math.pow(x,3) + math.pow(x,7)/99)
    elif (x < 203 and x >=153):
        return (54 * math.pow(x,7) + math.sin(x))
    elif (x < 295 and x >=203):
        return 77* math.pow((math.pow(x,5)-math.sin(x)),2) - x
    else:
        return math.exp(math.pow(x,3) + 84*x) - math.cos(x) + 27

print("{:.2e}".format(f12()))


