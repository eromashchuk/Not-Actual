bilet_n = int(input("Введите количество билетов: "))
total_price = 0
try:
    for i in range(1, bilet_n + 1):
        age = int(input(f"Введите возраст для {i} билета: "))
        if 0 <= age <= 18:
            price = 0
        elif 18 < age <= 25:
            price = 990
        else:
            price = 1395
        total_price += price
        i = i + 1

finally:
    if bilet_n > 3:
        print(f'Общая стоимость: {total_price} руб.')
        print(f'Стоимость со скидкой 10%: {total_price * 0.9} руб.')
    else:
        print(f'Общая стоимость: {total_price} руб.')
