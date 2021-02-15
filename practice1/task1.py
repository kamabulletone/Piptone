import math

def f11(x,y,z):

    a = (math.tan(94*(math.pow(x,4))) + math.pow(x,6)) / (math.pow(x,3) + 52 * math.pow(z,7))
    b = (math.exp(x) + math.pow(x,4)) / (77* math.pow(z,2) - 49*y)
    c = math.sqrt( (37*math.pow(z,8) + math.pow(y,4)/66)/ (math.pow(x,6) - y + 59) )
    return "{:.2e}".format(a-b+c)

##res = f
#print(f11(-90,47,-48))