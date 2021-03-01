#task 1
"""
s = ['235', '1223', '228']
a = [int(i) for i in s]
print(s)
print(a)
"""
#task 2
"""
s = ['235', '1223', '228', '228']
a = [len(set(s))]
print(a)
"""
#task 3
"""
s = ['235', '1223', '228', '228']
a = s[::-1]
print(a)
"""
#task 4
"""
s = ['235', '1223', '228', '228']
a = [i for i, j in enumerate(s) if j == '228']
print(a)
"""
#task 5
"""
s = [235, 1223, 228, 228, 1992]
a = sum([j for i, j in enumerate(s) if not i % 2])
print(a)
"""
#task 6
"""
s = ['235', '1223', '228', '228', 'VeryLongStr']
a = max([len(i) for i in s])
print(a)
"""