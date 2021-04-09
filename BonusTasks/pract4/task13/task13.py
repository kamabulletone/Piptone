
class Num:
    def __init__(self, num):
        self.num = num
    def ret_value(self):
        return self.num
    def ret_calc_value(self):
        return self.num
    def ret_num(self):
        return self.num
    def ret(self):
        return self.num
    def ret_op(self):
        return ''

class Add:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def ret_value(self):
        self.res = "(" + str(self.num1.ret_value()) + " + " + str(self.num2.ret_value()) + ")"

        return self.res
    def ret_calc_value(self):
        self.calc_res = self.num1.ret_calc_value() + self.num2.ret_calc_value()
        return self.calc_res

    def ret(self):
        str1 = str(self.num1.ret()) + '\n' + str(self.num2.ret())
        return str1
    def ret_op(self):
        str1 = 'ADD\n' + str(self.num1.ret_op()) + '\n' + str(self.num2.ret_op())
        return str1

class Mul:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def ret_value(self):
        self.res = "(" + str(self.num1.ret_value()) + " * " + str(self.num2.ret_value()) + ")"


        return self.res

    def ret_calc_value(self):
        self.calc_res = self.num1.ret_calc_value() * self.num2.ret_calc_value()
        return self.calc_res
    def ret(self):
        str1 = str(self.num1.ret()) + '\n' + str(self.num2.ret())
        return str1
    def ret_op(self):
        str1 = 'MUL\n' + str(self.num1.ret_op()) + '\n' + str(self.num2.ret_op())
        return str1


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
        self.res1 = exps.ret()
        self.res2 = exps.ret_op()
    def get_code(self):
        nums = self.res1.split("\n")
        nums = ["PUSH " + i for i in nums]
       # print(nums)
        ops = self.res2.split("\n")
        opsC = ops.count('')
        for i in range(opsC):
            ops.remove('')
        ops.reverse()
        res = '\n'.join(nums) + "\n" + "\n".join(ops)
        return  res







#ast = Add(Num(7), Mul(Num(3), Num(2)))
ast = Add( Mul( Add(Num(3), Num(10)), Add(Num(5), Num(3))), Num(5))
#ast = Mul(Mul(Num(3),Num(7)), Add(Num(5),Num(6)))
pv = PrintVisitor()
cv = CalcVisitor()
sv = StackVisitor()
print(pv.visit(ast))
print(cv.visit(ast))
sv.visit(ast)
print(sv.get_code())


