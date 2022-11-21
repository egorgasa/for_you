sec= input('Введите секунды: ')

while type(sec) != int:
    try:
        sec = int(sec)
        hour = sec // 3600
        sec %= 3600
        min = sec // 60
        sec %= 60
        print("%02d:%02d:%02d" % (hour, min, sec))
    except ValueError:
        print('Введите нормальное число')
        sec = input('Введите секунды: ')
