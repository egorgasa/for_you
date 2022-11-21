num = input('Введите любое целое положительное число: ')

while type(num) != int:
    try:
        num = int(num)
        if num < 0:
            print('Вы ввели число меньше нуля')
            num = input('Введите положительное число: ')
        else:
            num = str(num)
            break
    except ValueError:
        print('Вы ввели не число')
        num = input('Введите любое целое число: ')

result = list(num)
max_number = max(result)
print("Наибольшее число:", max_number)