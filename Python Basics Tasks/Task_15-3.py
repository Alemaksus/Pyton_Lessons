# Напишите функцию которая принимает на вход список. Функция создает из этого списка новый список
# из квадратных корней чисел (если число положительное) и самих чисел (если число отрицательное)
# и возвращает результат (желательно применить генератор и тернарный оператор при необходимости).
# В результате работы функции исходный список не должен измениться. Например:
# old_list = [1, -3, 4]
# result = [1, -3, 2]
# Примечание: Список с целыми числами создайте вручную в начале файла.
# Не забудьте включить туда отрицательные числа. 10-20 чисел в списке вполне достаточно.

import math

old_list = [1, -1, 2, -2, 4, 5, 6, 7, 8, 9]

def new_sqrt_list(input_list):

    # Метод через генератор и тернарный оператор:
    result = [math.sqrt(number) if number > 0 else number for number in input_list ]
    return result

    # Метод через range & цикл:

    # input_list = input_list.copy()
    # for i in range(len(input_list)):
    #     number = input_list[i]
    #     if number > 0:
    #         input_list[i] = math.sqrt(number)
    #     # else:
    #     #     del input_list[i]
    # return input_list

result = new_sqrt_list(old_list)
print(result)
print(old_list)