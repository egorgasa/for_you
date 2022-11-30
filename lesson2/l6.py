# 6) *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два
# элемента — номер товара и словарь с параметрами (характеристиками товара: название,
# цена, количество, единица измерения). Структуру нужно сформировать программно, т.е.
# запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ —
# характеристика товара, например название, а значение — список значений-характеристик,
# например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }
def input_tovar(num):
    name = input('Введите название: ')
    cost = input('Введите цену: ')

    while type(cost) != int:
        try:
            cost = int(cost)
        except ValueError:
            print('что-то не то ввели')
            cost = input('Введите цену: ')
    count = input('Введите кол: ')

    while type(count) != int:
        try:
            count = int(count)
        except ValueError:
            print('что-то не то ввели')
            count = input('Введите кол: ')

    unit = input('Введите eд: ')
    return (num, {'title': name, 'price': cost, 'amount': count, 'unit': unit})


def anal(products):
    analitics = {
        'title': [],
        'price': [],
        'amount': [],
        'unit': set()
    }
    for _, item in products:
        print(item['title'])
        analitics['title'].append(item['title'])
        analitics['price'].append(item['price'])
        analitics['amount'].append(item['amount'])
        analitics['unit'].add(item['unit'])

    print(analitics)

print('хай, будем делать товарку. готовься')

products = []

count = 0

while count < 2:
    count += 1
    products.append(input_tovar(count))

anal(products)