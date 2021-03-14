# 1. whitespace before '('.
for i in range (2):
    print(i)

# 2. missing whitespace around operator.
b= 5

# 3. missing whitespace after ','.
a = [5,6]

# 4. unexpected spaces around keyword / parameter equals.
def foo(k = 2, a = 3):
    print("a")

# 5. expected 2 blank lines, found 1.
def foo1():
    return

def foo2():
    return

# 6. multiple statements on one line (colon).
if a > 5: print("A")

# 7. multiple statements on one line (semicolon).
a = 5; b = 6

# 8. comparison to None should be 'if cond is None:'.
if a == None:
    print("A")

# 9. comparison to True should be 'if cond is True:' or 'if cond:'.
if a == True:
    print("A")