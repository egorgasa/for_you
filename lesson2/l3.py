# 3) Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года
# относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

seasons_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
seasons_time_year = {0: 'зима', 1: 'зима', 2: 'весна', 3: 'весна', 4: 'весна', 5: 'лето', 6: 'лето', 7: 'лето', 8: 'осень', 9: 'осень', 10: 'осень', 11: 'зима'}
month = input('введите месяц пж: ')
count_attempts = 0

while type(month) != int or count_attempts < 5:
    try:
        month = int(month)
        if month > 12 or month <= 0:
            print('такого месяц нет')
            raise Exception
        break
    except(ValueError, Exception):
        print('что-то не так')
        count_attempts += 1
        month = input('введите месяц пж: ')

print(seasons_time_year.get(seasons_number.index(month)))
