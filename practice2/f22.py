# 0x0a0e42cc

def f22(x):

    x = "{0:#0{1}x}".format(x,10)
   # print("x = " + x)

    op1 = int(x,16)
    #print(hex(op1))

    A = op1 & int("0b1111111111",2)
    A = "{0:#0{1}x}".format(A,5)
    Ab = f'{int(A,16):0>10b}'

   # print("A = " + A)
   # print("Ab = " + Ab)

    op1 = op1 >> 10
    #print(hex(op1))

    B = op1 & int("0b11111111111",2)
    B = "{0:#0{1}x}".format(B,5)
    Bb = f'{int(B,16):0>11b}'

    op1 = op1 >> 11
   # print("B = " + B)
   # print("Bb = " + Bb)

    C = op1 & int("0b1111111",2)
    C = "{0:#0{1}x}".format(C,4)
    Cb = f'{int(C,16):0>7b}'
    op1 = op1 >> 7


   # print("C = " + C)
  #  print("Cb = " + Cb)

    D = op1 & int("0b1",2)
    D = "{0:#0{1}x}".format(D,3)
    Db = f'{int(D,16):0>1b}'
    op1 = op1 >> 1

   # print("D = " + D)
  #  print("Db = " + Db)

    E = op1 & int("0b111",2)
    E = "{0:#0{1}x}".format(E,3)
    Eb = f'{int(E,16):0>3b}'
    op1 = op1 >> 3

   # print("E = " + E)
  #  print("Eb = " + Eb)

    res = [Ab,Bb,Cb,Db,Eb]

    # for i in res:
    #     print(i)

    resStr = "0b" + Eb + Bb + Db + Cb + Ab
  #  print(hex(int(resStr,2)))
    t = int(resStr,2)
    return "{0:#0{1}x}".format(t,10)









