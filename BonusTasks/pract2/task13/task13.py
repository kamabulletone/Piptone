
def generate_groups():
    groups_chars = ['К', 'В', 'М', 'Н']
    groups_count = [25, 13, 2, 10]
    for i, j in zip(groups_chars, groups_count):
        for k in range(1,j+1):
            print(i + str(k))


generate_groups()