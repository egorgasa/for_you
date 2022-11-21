a = input('Введи сколько пробежал в первый день')

while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        a = input('Введи норм км')

b = input('не мнее скольки надо')

while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        b = input('Введи норм км')

i = 1;
new_b = b * 1.1
while a < new_b:
    print(f'{i}-й день: {round(a, 2)}')
    a *= 1.1
    i += 1

print(f'спортик достиг результата — не менее {b} км на {i-1}-й день')