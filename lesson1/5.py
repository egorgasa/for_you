def how_many_slaves():
    empl = input('Скажи пж сколько сколько у тебя рабов ?')

    while type(empl) != int:
        try:
            empl = int(empl)
            if empl < 0:
                print('Ты сам у себя раб ? последний раз спрашиваю, сколько ???')
                empl = input('Введите положительное число по братски: ')
        except ValueError:
            print('Хочу больше')
            empl = input('Рабов сколько спрашиваю')
    money = (vir - izder) // empl
    print(f'в среднем раб тебе приносит чистой прибыли {money} рупей')


vir = input('Введите пж выручку')

while type(vir) != int:
    try:
        vir = int(vir)
    except ValueError:
        print('Вы ввели какое-то странное число) давай повторим')
        vir = input('Введите пж выручк')

izder = input('Введите пж издержки')

while type(izder) != int:
    try:
        izder = int(izder)
    except ValueError:
        print('Вы ввели какое-то странное число) давай повторим')
        izder = input('Введите пж издержки')

print('Красава. ты все ввел правильно, едем далей')

if vir > izder:
    print('Ты знал что ты богат, у тебя прибыиль, надо делиться')
    how_many_slaves()
elif vir == izder:
    print('работаешь в 0,л*х')
    how_many_slaves()
else:
    print('Работай лучше. ты в минусе и тебя ищут за долги')
