import random
r = random
print("Тренировка Умножения")
while yours_c != 1!:
    a = r.randint(2, 9)
    b = r.randint(2, 9)
    c = a * b
    yours_c = eval(input(f"Сколько будет {a} * {b}? "))
    if yours_c == c:
        print("Правильно!")
    else:
        print("Неправильно!")
