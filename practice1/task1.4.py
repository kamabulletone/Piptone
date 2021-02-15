import math


def count(n):
    if (n == 0):
        return 2
    elif (n == 1):
        return 2
    else:
        return (math.pow(count(n - 1), 2) / 87) - abs(count(n - 1))

def f14(n):
    return "{:.2e}".format(count(n))


print(f14(13))
