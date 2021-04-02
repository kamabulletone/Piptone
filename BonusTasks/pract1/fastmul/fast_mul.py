
x = int(input("x = "))
y = int(input("y = "))



def fast_mul(x,y):

    # Если оба числа 0, то возвращаем сразу результат 0
    if (x == 0 and y == 0):
        return 0

    xlist = div2(x)
    ylist = mul2(y, len(xlist))
    sum = 0
    # 1-ый лист - первое число, содержащий результаты последовательного деления на 2
    # 2-ый лист - второе число, содержащий результаты последовательного умножения на 2
    # Складываем те числа из 2го листа, где под его порядковым номером i лежит нечетное значение в 1м листе.
    for i in range(len(xlist)):
        if (xlist[i] % 2 != 0):
            sum += ylist[i]

    #print(xlist)
   # print(ylist)
    return sum


# Функция, которая возвращает лист, состоящий из входного числа последовательно деленного на два
def div2(num):
    resList = [num]

    while num > 0:
        temp = num // 2
        num = num // 2
        resList.append(temp)

    return resList

#Функция, которая возвращает лист, состоящий входного числа последовательно умноженного на два
def mul2(num, length):
    resList = [num]
    for i in range(length-1):
        num *= 2
        resList.append(num)
    return resList

print(fast_mul(x,y))
