# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# Мой варик (недоделанный):

# m = int(input('Введите месяц цифрой: '))
# if m [3:5]:
#     print('весна')
#     elif m [6:8]:
#     print('лето')
#     elif m [9-11]:
#     print('осень')
#     else
#     print('зима')

# Вариант Евгения:

while True:
    user_month = input('Введите номер месяца от 1 до 12: ')
    if user_month.isdigit() and 0 <= int(user_month) <= 12:
    # if 0 <= int(user_month) <= 12 and user_month.isdigit():
        season_1 = ['зима', 'весна', 'лето', 'осень', 'зима']
        season_1 = {0: 'зима', 1: 'весна', 2: 'лето', 3: 'осень', 4: 'зима'}
        print(f'Список сезонов - {season_1[int(user_month) // 3]}\nСловарь сезонов - {season_1[int(user_month) // 3]}')
        break
    else:
        print('Ошибка')


