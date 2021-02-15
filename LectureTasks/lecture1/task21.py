
def naive_mul(x, y):
    if x == 0 or y == 0:
        return 0
    r = x
    for i in range(0, y - 1):
        x = x + r
    return x


print(naive_mul(10, 15))