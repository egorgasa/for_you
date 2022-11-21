number = input('Введите число: ')
sequence_number = 3
suma = 0

while type(number) != int:
    try:
        number = int(number)
        for i in range(1, number + 1):
            suma += sequence_number
            sequence_number = (sequence_number * 10) + 3
    except ValueError:
        print('Вы ввели не число')
        number = input("Введите число :")

print(f'Итого {suma}')
