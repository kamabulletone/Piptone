#task 1
"""
s = ['23', '123', '1337']
a = [int(i) for i in s]
print(s)
print(a)
"""
#task 2
"""
s = ['23', '123', '1337', '1337']
a = [len(set(s))]
print(a)
"""
#task 3
"""
s = ['23', '123', '1337', '1337']
a = s[::-1]
print(a)
"""
#task 4
"""
s = ['23', '123', '1337', '1337']
a = [i for i, j in enumerate(s) if j == '1337']
print(a)
"""
#task 5
"""
s = [23, 123, 1337, 1337, 1992]
a = sum([j for i, j in enumerate(s) if not i % 2])
print(a)
"""
#task 6
"""
s = ['23', '123', '1337', '1337', 'VeryLongStr']
a = max([len(i) for i in s])
print(a)
"""