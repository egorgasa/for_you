name = input('Введите имя: ')
surname = input('Введите фамилию: ')
age = input('Сколько вам лет ? ')

while type(age) != int:
    try:
        age = int(age)
    except ValueError:
        print('вы ввели не число, введите число пж')
        age = input('Сколько вам лет ?')

print(f'Вы {name} {surname} и вам {age}')
