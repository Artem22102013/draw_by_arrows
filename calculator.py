a = eval(input("A число: "))
b = eval(input("B число: "))
op = input("Op: ")
if op == '+':
    c = a + b
if op == '-':
    c = a - b
if op == '*':
    c = a * b
if op == '/':
    c = a / b
print(c)
