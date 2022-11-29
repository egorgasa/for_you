# 4) Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое
# слово с новой строки. Строки необходимо пронумеровать. Если в слово длинное, выводить
# только первые 10 букв в слове.


str = input('Введите несколько слов через пробел ').split()
count_attempts = 0
while count_attempts < 5:
    try:
        if len(str) <= 1:
            print('мало')
            raise Exception
        break
    except (Exception):
        count_attempts += 1
        str = input('Введите несколько слов через пробел ').split()

for i, j in enumerate(str):
    print(f'слово {j[0:9]} было введено {i+1}')
