import random
# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно 
# перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

# quan_elem = int(input("Enter number of elements: "))
# # 1 - Это решка
# # 0 - Это герб
# dices_list = [random.randint(0,1) for i in range(quan_elem)]
# print(dices_list)

# head_needed = 0
# tail_needed = 0

# for i in dices_list:
#     if i == 1:
#         tail_needed += 1
#     else:
#         head_needed += 1

# if head_needed < tail_needed:
#     print(f"Minimum number of coins: {head_needed}")
# else:
#     print(f"Minimum number of coins: {tail_needed}")


# ----------------------------------------------------------------------------------------

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих 
# чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# num_x = random.randint(0, 1001)
# num_y = random.randint(0, 1001)

# numbers = [num_x, num_y]

# print(f"Guessed: Number x = {numbers[0]} and number y = {numbers[1]}")

# find_num_x = 0
# find_num_y = 0

# # for i in numbers:
# #     for j in numbers:
# #         if i + j == (num_x + num_y) and i * j == (num_x * num_y):
# #             find_num_x = j
# #             find_num_y = i

# print(f"Result: number X = {find_num_x} and number Y = {find_num_y}")

# ------------------------------------------------------------------------------------

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.

# num_n = int(input("Enter number: "))
# i = 0
# while 2 ** i <= num_n:
#     print(2 ** i)
#     i += 1