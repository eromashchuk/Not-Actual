'''Напишите программу, которой:
 1. на вход подается последовательность чисел через пробел,
 2. также запрашивается у пользователя любое число.
 3. проверка соответствия указанному в условии ввода данных.
   Далее программа работает по следующему алгоритму:
4. Преобразование введённой последовательности в список
5. Сортировка списка по возрастанию элементов в нем (для реализации сортировки определите функцию)
6. Устанавливается номер позиции элемента, который меньше введенного пользователем числа,
   а следующий за ним больше или равен этому числу.
7. При установке позиции элемента воспользуйтесь алгоритмом двоичного поиска,
   который был рассмотрен в этом модуле.
   Реализуйте его также отдельной функцией.
8. Подсказка: есть числа, которые могут не соответствовать заданному условию.
   В этом случае необходимо вывести соответствующее сообщение
9. Для проверки загрузите полученное решение на GitHub и прикрепите ссылку.'''

def task_17_9_1():
    try:
        user_input = input("Введите последовательность чисел через пробел: ")
        user_num = int(input("Введите любое число: "))
        user_list = list(set(list(map(int, user_input.split()))))
    except ValueError as error:
        print("Ошибка: Неверное значение, допустим только ввод чисел")
    finally:
        def sort_user_data():
            for i in range(len(user_list)):  # проходим по всему массиву
                idx_min = i  # сохраняем индекс предположительно минимального элемента
                for j in range(i, len(user_list)):
                    if user_list[j] < user_list[idx_min]:
                        idx_min = j
                if i != idx_min:  # если индекс не совпадает с минимальным, меняем
                    user_list[i], user_list[idx_min] = user_list[idx_min], user_list[i]
            return user_list
        sort_user_data()

        l = user_list[0]
        r = user_list[-1]

        def binary_search(user_list, user_num, l, r):
            if l > r:  # если левая граница превысила правую,
                return False  # значит элемент отсутствует

            middle = (r + l) // 2  # находимо середину
            if user_list[middle] == user_num:  # если элемент в середине,
                return middle  # возвращаем этот индекс
            elif user_num < user_list[middle]:  # если элемент меньше элемента в середине
                # рекурсивно ищем в левой половине
                return binary_search(user_list, user_num, l, middle - 1)
            else:  # иначе в правой
                return binary_search(user_list, user_num, middle + 1, r)

        print(binary_search(user_list, user_num, l, r))

task_17_9_1()


