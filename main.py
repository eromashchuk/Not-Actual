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
# from math import log
# a = 10000 * log(10000,2)
# b = 10000 ** 2
# print(a)
# print(b)
# print(b/a)

# def p(n):
#     if n == 0:
#         return f"0"
#     else:
#         print(n)
#         return p(n-1)
#
# print(p(5))

# def p(n):
#     if n == 0:
#         return f"0"
#     else:
#         p(n-1)
#         print(n)
#
# print(p(5))

# def par_checker(string):
#     stack = []  # инициализируем стек
#
#     for s in string:  # читаем строку посимвольно
#         if s == "(":  # если открывающая скобка,
#             stack.append(s)  # добавляем её в стек
#         elif s == ")":
#             # если встретилась закрывающая скобка, то проверяем
#             # пуст ли стек и является ли верхний элемент — открывающей скобкой
#             if len(stack) > 0 and stack[-1] == "(":
#                 stack.pop()  # удаляем из стека
#             else:  # иначе завершаем функцию с False
#                 return False
#     # если стек пустой, то незакрытых скобок не осталось
#     # значит, возвращаем True, иначе — False
#     return len(stack) == 0
# print(par_checker('(5+6)*(7+8)/(4+3)'))

# pars = {")": "(", "]": "["}
# def par_checker_mod(string):
#     stack = []
#
#     for s in string:
#         if s in "([":
#             stack.append(s)
#         elif s in ")]":
#             if len(stack) > 0 and stack[-1] == pars[s]:
#                 stack.pop()
#             else:
#                 return False
#     return len(stack) == 0
#
# G = {"Адмиралтейская" :
#          {"Садовая" : 4},
#      "Садовая" :
#          {"Сенная площадь" : 3,
#           "Спасская" : 3,
#           "Адмиралтейская" : 4,
#           "Звенигородская" : 5},
#      "Сенная площадь" :
#          {"Садовая" : 3,
#           "Спасская" : 3},
#      "Спасская" :
#          {"Садовая" : 3,
#           "Сенная площадь" : 3,
#           "Достоевская" : 4},
#      "Звенигородская" :
#          {"Пушкинская" : 3,
#           "Садовая" : 5},
#      "Пушкинская" :
#          {"Звенигородская" : 3,
#           "Владимирская" : 4},
#      "Владимирская" :
#          {"Достоевская" : 3,
#           "Пушкинская" : 4},
#      "Достоевская" :
#          {"Владимирская" : 3,
#           "Спасская" : 4}}

# D = {k: 100 for k in G.keys()} # расстояния
# start_k = 'Адмиралтейская' # стартовая вершина
# D[start_k] = 0 # расстояние от неё до самой себя равно нулю
# U = {k : False for k in G.keys()} # флаги просмотра вершин
# P = {k : None for k in G.keys()}
# for _ in range(len(D)):
#     # выбираем среди непросмотренных наименьшее по расстоянию
#     min_k = min([k for k in U.keys() if not U[k]], key=lambda x: D[x])
#
#     for v in G[min_k].keys(): # проходимся по всем смежным вершинам
#          if D[v] > D[min_k] + G[min_k][v]: # если расстояние от текущей вершины меньше
#             D[v] = D[min_k] + G[min_k][v] # то фиксируем его
#             P[v] = min_k # и записываем как предок
#     U[min_k] = True # просмотренную вершину помечаем
# pointer = 'Владимирская' # куда должны прийти
# while pointer is not None: # перемещаемся, пока не придём в стартовую точку
#     print(pointer)
#     pointer = P[pointer]
# print(P)

# class BinaryTree:
#     def __init__(self, value):
#         self.value = value
#         self.left_child = None
#         self.right_child = None
#
#
#     def insert_left(self, next_value):
#         if self.left_child is None:
#             self.left_child = BinaryTree(next_value)
#         else:
#             new_child = BinaryTree(next_value)
#             new_child.left_child = self.left_child
#             self.left_child = new_child
#         return self
#
#     def insert_right(self, next_value):
#         if self.right_child is None:
#             self.right_child = BinaryTree(next_value)
#         else:
#             new_child = BinaryTree(next_value)
#             new_child.right_child = self.right_child
#             self.right_child = new_child
#         return self
#
#     def pre_order(self):
#         print(self.value)  # процедура обработки
#
#         if self.left_child is not None:  # если левый потомок существует
#             self.left_child.pre_order()  # рекурсивно вызываем функцию
#
#         if self.right_child is not None:  # если правый потомок существует
#             self.right_child.pre_order()  # рекурсивно вызываем функцию
#
#     def post_order(self):
#         if self.left_child is not None:  # если левый потомок существует
#             self.left_child.post_order()  # рекурсивно вызываем функцию
#
#         if self.right_child is not None:  # если правый потомок существует
#             self.right_child.post_order()  # рекурсивно вызываем функцию
#
#         print(self.value)  # процедура обработки
#
#     def in_order(self):
#         if self.left_child is not None:  # если левый потомок существует
#             self.left_child.in_order()  # рекурсивно вызываем функцию
#
#         print(self.value)  # процедура обработки
#
#         if self.right_child is not None:  # если правый потомок существует
#             self.right_child.in_order()  # рекурсивно вызываем функцию
#
# root_node = BinaryTree(2).insert_left(7).insert_right(5)
# l_node_7 = root_node.left_child.insert_left(2).insert_right(6)
# l_node_6 = l_node_7.right_child.insert_left(5).insert_right(11)
# r_node_5 = root_node.right_child.insert_right(9)
# r_node_9 = r_node_5.right_child.insert_left(4)
#
# root_node.in_order()

# ------
# class Node:  # класс элемента
#     def __init__(self, value=None, next_=None):  # инициализируем
#         self.value = value  # значением
#         self.next = next_  # и ссылкой на следующий элемент
#
#     def __str__(self):
#         return "Node value = " + str(self.value)
#
#
# class LinkedList:  # класс списка
#     def __init__(self):  # инициализируем пустым
#         self.first = None
#         self.last = None
#
#     def clear(self):  # очищаем список
#         self.__init__()
#
#     def __str__(self):  # функция печати
#         R = ''
#
#         pointer = self.first  # берем первый указатель
#         while pointer is not None:  # пока указатель не станет None
#             R += str(pointer.value)  # добавляем значение в строку
#             pointer = pointer.next  # идем дальше по указателю
#             if pointer is not None:  # если он существует добавляем пробел
#                 R += ' '
#         return R
#
#     def pushleft(self, value):
#         if self.first is None:
#             self.first = Node(value)
#             self.last = self.first
#         else:
#             new_node = Node(value, self.first)
#             self.first = new_node
#
#     def pushright(self, value):
#         if self.first is None:
#             self.first = Node(value)
#             self.last = self.first
#         else:
#             new_node = Node(value)
#             self.last.next = new_node
#             self.last = new_node
#
#     def popleft(self):
#         if self.first is None:  # если список пустой, возвращаем None
#             return None
#         elif self.first == self.last:  # если список содержит только один элемент
#             node = self.first  # сохраняем его
#             self.__init__()  # очищаем
#             return node  # и возвращаем сохраненный элемент
#         else:
#             node = self.first  # сохраняем первый элемент
#             self.first = self.first.next  # меняем указатель на первый элемент
#             return node  # возвращаем сохраненный
#
#     def popright(self):
#         if self.first is None:  # если список пустой, возвращаем None
#             return None
#         elif self.first == self.last:  # если список содержит только один элемент
#             node = self.first  # сохраняем его
#             self.__init__()  # очищаем
#             return node  # и возвращаем сохраненный элемент
#         else:
#             node = self.last  # сохраняем последний
#             pointer = self.first  # создаем указатель
#             while pointer.next is not node:  # пока не найдем предпоследний
#                 pointer = pointer.next
#             pointer.next = None  # обнуляем указатели, чтобы
#             self.last = pointer  # предпоследний стал последним
#             return node  # возвращаем сохраненный
#
#     def __iter__(self):  # объявляем класс как итератор
#         self.current = self.first  # в текущий элемент помещаем первый
#         return self  # возвращаем итератор
#
#     def __next__(self):  # метод перехода
#         if self.current is None:  # если текущий стал последним
#             raise StopIteration  # вызываем исключение
#         else:
#             node = self.current  # сохраняем текущий элемент
#             self.current = self.current.next  # совершаем переход
#             return node  # и возвращаем сохраненный
#
#     def __len__(self):
#         count = 0
#         pointer = self.first
#         while pointer is not None:
#             count += 1
#             pointer = pointer.next
#         return count
# LL = LinkedList()
#
# LL.pushright(1)
# LL.pushleft(2)
# LL.pushright(3)
# LL.popright()
# LL.pushleft(4)
# LL.pushright(5)
# LL.popleft()
#
# print(LL.__len__())

# ----------

# def find(array, element):
#     for i, a in enumerate(array):
#         if a == element:
#             return i
#     return False
#
# array = list(map(int, input().split()))
# element = int(input())
#
# print(find(array, element))
#
# def count(array, element):
#     count = 0
#     for a in array:
#         if a == element:
#             count += 1
#     return count
#
#
# def binary_search(array, element, left, right):
#     if left > right:  # если левая граница превысила правую,
#         return False  # значит элемент отсутствует
#
#     middle = (right + left) // 2  # находимо середину
#     if array[middle] == element:  # если элемент в середине,
#         return middle  # возвращаем этот индекс
#     elif element < array[middle]:  # если элемент меньше элемента в середине
#         # рекурсивно ищем в левой половине
#         return binary_search(array, element, left, middle - 1)
#     else:  # иначе в правой
#         return binary_search(array, element, middle + 1, right)
#
#
# element = int(input())
# array = [i for i in range(1, 100)]  # 1,2,3,4,...
#
# # запускаем алгоритм на левой и правой границе
# print(binary_search(array, element, 0, 99))

# array = '93 326 215 443 944 152 681 699 238 856 266 700 490 715 968 264 381 621 468 592 963 895 217 599 993 229 915 608 941 463 976 156 518 286 253 697 920 827 223 758 251 185 210 916 864 000 000 000 000 000 000 000 000'
# li = []
# s = ""
# for i in array:
#     if i != " ":
#         li.append(i)
# print(len(s.join(li)))

# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
# n = []
# for i in range(1, len(array)):
#     x = array[i]
#     idx = i
#     while idx > 0 and array[idx-1] > x:
#         array[idx] = array[idx-1]
#         idx -= 1
#     array[idx] = x
# print(x)
# print(idx)
#
# def binary_search(array, element, left, right):
#     if left > right:  # если левая граница превысила правую,
#         return False  # значит элемент отсутствует
#
#     middle = (right + left) // 2  # находимо середину
#     if array[middle] == element:  # если элемент в середине,
#         return middle  # возвращаем этот индекс
#     elif element < array[middle]:  # если элемент меньше элемента в середине
#         # рекурсивно ищем в левой половине
#         return binary_search(array, element, left, middle - 1)
#     else:  # иначе в правой
#         return binary_search(array, element, middle + 1, right)
#
#
# element = int(input())
# array = [i for i in range(1, 100)]  # 1,2,3,4,...
#
# # запускаем алгоритм на левой и правой границе
# print(binary_search(array, element, 0, 99))
