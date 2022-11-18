# Допишите функцию check_user так, чтобы она по логину пользователя
# проверяла, существует он или нет,
# после чего с помощью вложенного условия проверяла
# правильность пароля этого пользователя.
# Функция должна возвращать только True или False.
# Чтобы вернуть True, напишите "return True";
# чтобы вернуть False, напишите "return False".
#
# user_database = {
#     'user': 'password',
#     'iseedeadpeople': 'greedisgood',
#     'hesoyam': 'tgm'
# }
#
# def check_user(username, password):
#     if username in user_database:
#         if password == user_database[username]:
#             return True
#         else:
#             return False
#     else:
#         return False
#
# print(check_user('iseedeadpeople', 'greedisgood'))
from numpy._distributor_init import filename

# a = 15
# if -10 <= a <= -1 or 2 <= a <= 15:
#     print('True')
# else:
#     print('False')
#
# n = 25
# first_digit = n // 10
# second_digit = n % 10
#
# print((first_digit == 5) or (second_digit == 5))

# S = 0  # заводим переменную-счетчик, в которой мы будем считать сумму
# N = 5

# заводим цикл for, в котором мы будем проходить по всем числам от одного до N
# for i in range(1, N + 1):  # равносильно выражению for i in [1, 2, 3, ... , N -1, N]:
#     print("Значение суммы на предыдущем шаге: ", S)
#     print("Текущее число: ", i)
#     S = S + i  # cуммируем текущее число i и перезаписываем значение суммы
#     print("Значение суммы после сложения: ", S)
#     print("---")
# print("Конец цикла")
# print()
# print("Ответ: сумма равна = ", S)


# Напишите цикл с использованием бесконечного цикла whilе с постусловием, который возводит натуральные числа в квадрат, пока результат меньше 1000.
# n = 1
# while True:
#    if n ** 2 >= 1000:
#        print("Последнее число", n - 1)
#        break
#    n += 1
#
# list_ = [-5, 2, 4, 8, 12, -7, 5]
# # Объявим переменную, в которой будем хранить индекс отрицательного элемента
# index_negative = None
#
# for i, value in enumerate(list_):
#     if value < 0:
#         print("Отрицательное число: ", list_[i])
#         index_negative = i  # перезаписываем значение индекса
#         print("Новый индекс отрицательного числа: ", index_negative)
#     else:
#         print("Положительное число: ", list_[i])
#     print("---")
# print("Конец цикла")
# print()
# print("Ответ: индекс последнего отрицательного элемента = ", index_negative)
#
# heads = 35  # количество голов
# legs = 94  # количество ног
#
# for r in range(heads + 1):  # количество кроликов
#     for ph in range(heads + 1):  # количество фазанов
#         #  если суммарное количество голов превышено или ног превышено, то переходим на следующий шаг цикла
#         if (r + ph) > heads or \
#             (r * 4 + ph * 2) > legs:
#             continue
#         if (r + ph) == heads and (r * 4 + ph * 2) == legs:
#             print("Количество кроликов", r)
#             print("Количество фазанов", ph)
#             print("---")
# try:
#     bilet_n = int(input("Введите количество билетов: "))
#     total_price = 0
#     for i in range(1, bilet_n + 1):
#         age = int(input(f"Введите возраст для {i} билета: "))
#         if 0 <= age <= 18:
#             price = 0
#         elif 18 < age <= 25:
#             price = 990
#         else:
#             price = 1395
#         total_price += price
#         i = i + 1
# except ValueError as error:
#     print("Ошибка: Неверное значение, введите число")
# finally:
#     if bilet_n > 3:
#         print(f'Общая стоимость: {total_price} руб.')
#         print(f'Стоимость со скидкой 10%: {total_price * 0.9} руб.')
#     else:
#         print(f'Общая стоимость: {total_price} руб.')

# def down_stairs_asterisks(num):
#     while num > 0:
#         print('*' * num)
#         num -= 1
# down_stairs_asterisks(10)

# def num_a(a):
#     d = 1
#     count = 0
#     while d <= a:
#         if a % d == 0:
#             count += 1
#         else:
#             None
#         d = d + 1
#
#     print(count)

# def is_palindrom(text):
#     text = str(text).lower()
#     text = text.replace(" ", "")
#
#     if text == text[::-1]:
#         return True
#     else:
#         return False
#
# print(is_palindrom("Кит на море не романтик"))

# def count(start=1, step=1):
#     counter = start
#     while True:
#         yield counter
#         counter += step
# count(5,1)
#
# def repeat_list(list_):
#    list_values = list_.copy()
#    while True:
#        value = list_values.pop(0)
#        list_values.append(value)
#        yield value
#
# for i in repeat_list([1, 2, 3]):
#    print(i)
#
# import time
#
# N = 100
#
#
# def decorator_time(fn):
#    def wrapper():
#        t0 = time.time()
#        result = fn()
#        dt = time.time() - t0
#        return dt
#    return wrapper
#
#
# def pow_2():
#    return 10000000 ** 2
#
#
# def in_build_pow():
#    return pow(10000000, 2)

#
# pow_2 = decorator_time(pow_2)
# in_build_pow = decorator_time(in_build_pow)
#
# mean_pow_2 = 0
# mean_in_build_pow = 0
# for _ in range(N):
#    mean_pow_2 += pow_2()
#    mean_in_build_pow += in_build_pow()
#
# print(f"Функция {pow_2} выполнялась {N} раз. Среднее время: {mean_pow_2 / N:.10f}")
# print(f"Функция {in_build_pow} выполнялась {N} раз. Среднее время: {mean_in_build_pow / 100:.10f}")
#
# def counter(func):
#    count = 0
#    def wrapper(*args, **kwargs):
#        nonlocal count
#        func(*args, **kwargs)
#        count += 1
#        print(f"Функция {func} была вызвана {count} раз")
#    return wrapper
#
# @counter
# def say_word(word):
#    print(word)
#
# say_word("Oo!!!")
# Oo!!!
# Функция <function say_word at 0x7f93836d47b8> была вызвана 1 раз
#
# say_word("Oo!!!")
# Oo!!!x
# Функция <function say_word at 0x7f93836d47b8> была вызвана 2 раз

# a = ["asd", "bbd", "ddfa", "mcsa"]
#
# print(list(map(len, a)))

# def quadratic_solve(a,b,c):
#     if D(a,b,c) < 0:
#         return "Нет вещественных корней"
#     elif D(a,b,c) == 0:
#         return -b/(2*a)
#     else:
#         return (-b-D(a,b,c)**0.5)/(2*a), (-b+D(a,b,c)**0.5)/(2*a)
#
# L = list(map(float, input().split()))
# quadratic_solve(*L)
#
# import os
# path_v = os.path.join('Users', 'chudi', 'Environments', 'filename.txt')
# pva = os.path.abspath(r"C:\Users\chudi\Environments\TestProjectSkillF\filename.txt")
#
# myFile = open(pva, "w+")
# myFile.write('ttttttt')
# print('zzzz', file=myFile)
# myFile.close()
# myFile = open(r"C:\Users\chudi\Environments\TestProjectSkillF\filename.txt", "r")
# print(myFile.read())
# myFile.close()
# print(pva)
#
# import json
#
# with open('json_example.json', encoding='utf8') as f:
#     template = {
#         'firstname': 'Иван',
#         'lastname': 'Иванов',
#         'isAlive': True,
#         'age': 32,
#         'address': {
#             'streetAddress': 'Нейбута 32',
#             'city': 'Владивосток',
#             'state': '',
#             'postalcode': ''
#         },
#         'phoneNumbers': [
#             {
#                 'type': 'mob',
#                 'number': '123-333-4455'
#             },
#             {
#                 'type': 'office',
#                 'number': '123 111-4567'
#             }
#         ],
#         'children': [],
#         'spouse': None
#     }
#
#     with open('to_json_example.json', 'w', encoding='utf8') as f:
#         json.dump(template, f, ensure_ascii=False, indent=4)
#
#     with open('to_json_example.json', encoding='utf8') as f:
#         print(f.read())

print(2 % 100)