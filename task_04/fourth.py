n = int(input('Введите номер накопителя: ')) - 1
if n < 7:


    list_dictov = [
        {'total': 999641890816, 'used': 228013805568},
        {'total': 61686008768, 'used': 52522710872},
        {'total': 149023482194, 'used': 83612310700},
        {'total': 498830397039, 'used': 459995976927},
        {'total': 93386008768, 'used': 65371350065},
        {'total': 988242468378, 'used': 892424683789},
        {'total': 49705846287, 'used': 9522710872},
    ]
    quantity = ((((int(list_dictov[n]['total']) - int(list_dictov[n]['used'])) / 1024) / 1024) / 1024)
    percent = 100 - ((int(list_dictov[n]['used']) / int(list_dictov[n]['total'])) * 100)
    print(f'Места осталость {round(quantity, 2)} Гб а в процентах это {round(percent,2)} %')
    if quantity < 10 or percent < 5:
        print(f'На накопителе {n + 1} критически мало свободного места')
    elif 30 > quantity > 10 or percent < 10:
        print(f'На накопителе {n + 1} мало свободного места')
    else:
        print(f'На накопителе {n + 1} достаточно свободного места')
else:
    print('Нет у нас столько винтов!!!')
