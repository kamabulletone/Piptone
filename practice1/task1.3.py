import math


def f13(n,m):
    summa = 0
    sum1 = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            summa += float(math.tan(j) + 94 * (i ** 7))
        sum1 += float(i + 52 * (i ** 3))
    return "{:.2e}".format(float(42 * summa - sum1))



#print(f13(40,71))

