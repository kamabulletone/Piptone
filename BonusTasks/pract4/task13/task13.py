
class Num:
    def __init__(self, num):
        self.num = num
    def ret_value(self):
        return self.num
    def ret_calc_value(self):
        return self.num

class Add:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def ret_value(self):
        self.res = "(" + str(self.num1.ret_value()) + " + " + str(self.num2.ret_value()) + ")"
        print(self.res)
        return self.res
    def ret_calc_value(self):
        self.calc_res = self.num1.ret_calc_value() + self.num2.ret_calc_value()
        return self.calc_res

class Mul:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def ret_value(self):
        self.res = "(" + str(self.num1.ret_value()) + " * " + str(self.num2.ret_value()) + ")"
        print(self.res)

        return self.res

    def ret_calc_value(self):
        self.calc_res = self.num1.ret_calc_value() * self.num2.ret_calc_value()
        return self.calc_res

class PrintVisitor:
    def __init__(self):
        pass
    def visit(self, exps):
        res = str(exps.ret_value())
        return res

class CalcVisitor:
    def __init__(self):
        pass
    def visit(self, exps):
        res = str(exps.ret_calc_value())
        return res

class StackVisitor():
    def __init__(self):
        pass
    def visit(self, exps):



ast = Add(Num(7), Mul(Num(3), Num(2)))
pv = PrintVisitor()
cv = CalcVisitor()
sv = StackVisitor()
print(pv.visit(ast))
print(cv.visit(ast))
sv.visit(ast)
print(sv.get_code())


