def transpose(x):
    return [list(i) for i in zip(*x)]


a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transpose(a))
