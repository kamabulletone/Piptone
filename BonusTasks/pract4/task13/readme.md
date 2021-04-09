
## **Работа с деревьями выражений**

1. Реализовать классы Num, Add, Mul.
2. Реализовать класс-посетитель PrintVisitor для печати выражения. Обойтись без операторов ветвления.
3. Реализовать класс-посетитель CalcVisitor для вычисления выражения. Обойтись без операторов ветвления.
4. Реализовать класс-посетитель StackVisitor для порождения кода стековой машины по выражению. Обойтись без операторов ветвления.
5. Добавьте классы Sub и Mul. В существующий код можно только добавлять новые строки, не изменяя старой части.

Пример:
```python
ast = Add(Num(7), Mul(Num(3), Num(2)))
pv = PrintVisitor()
cv = CalcVisitor()
sv = StackVisitor()
print(pv.visit(ast))
print(cv.visit(ast))
sv.visit(ast)
print(sv.get_code())
```
Результат:

```python
(7 + (3 * 2))
13
PUSH 7
PUSH 3
PUSH 2
MUL
ADD
```
Тестирование других данных:

Пример 1:
```
ast = Mul(Mul(Num(3),Num(7)), Add(Num(5),Num(6)))
pv = PrintVisitor()
cv = CalcVisitor()
sv = StackVisitor()
print(pv.visit(ast))
print(cv.visit(ast))
sv.visit(ast)
print(sv.get_code()) ```

Результат:
```python
((3 * 7) * (5 + 6))
231
PUSH 3
PUSH 7
PUSH 5
PUSH 6
ADD
MUL
MUL
```
___
Пример 2:
```python
ast = Add( Mul( Add(Num(3), Num(10)), Add(Num(5), Num(3))), Num(5))
pv = PrintVisitor()
cv = CalcVisitor()
sv = StackVisitor()
print(pv.visit(ast))
print(cv.visit(ast))
sv.visit(ast)
print(sv.get_code())
```
Результат:
```python
(((3 + 10) * (5 + 3)) + 5)
109
PUSH 3
PUSH 10
PUSH 5
PUSH 3
PUSH 5
ADD
ADD
MUL
ADD
```


