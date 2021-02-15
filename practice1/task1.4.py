import math


def f14(n):
    if (n == 0):
        return 2
    elif (n == 1):
        return 2
    else:
        return (math.pow(f14(n - 1), 2) / 87) - abs(f14(n - 1))


#print("{:.2e}".format(f14(13)))
