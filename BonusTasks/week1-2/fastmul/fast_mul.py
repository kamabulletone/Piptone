
x = int(input("x = "))
y = int(input("y = "))



def fast_mul(x,y):

    if (x == 0 and y == 0):
        return 0

    xlist = div2(x)
    ylist = mul2(y, len(xlist))
    sum = 0
    for i in range(len(xlist)):
        if (xlist[i] % 2 != 0):
            sum += ylist[i]

    #print(xlist)
   # print(ylist)
    return sum



def div2(num):
    resList = [num]

    while num > 0:
        temp = num // 2
        num = num // 2
        resList.append(temp)

    return resList

def mul2(num, length):
    resList = [num]
    for i in range(length-1):
        num *= 2
        resList.append(num)
    return resList

print(fast_mul(x,y))
