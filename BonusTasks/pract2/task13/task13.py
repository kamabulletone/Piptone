
def generate_groups():
    groups_chars = ['К', 'В', 'М', 'Н']
    groups_count = [25, 13, 2, 10]
    res = []
    for i, j in zip(groups_chars, groups_count):
        for k in range(1,j+1):
            res.append(i + str(k))
    return res

print(generate_groups())