# Домашнее задание - 3
# Задача-3

# Задайте список из вещественных чисел. Напишите программу, которая 
# найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
x=[round(random.uniform(2, 100), 2) for x in range(5)]
print(f'создаем случайный список из 5 элементов =>{x}')

x2=[]
i = 0
while i < len(x):
    y = round(x[i]%1, 2)
    x2.append(y)
    i += 1
print(f'убираем дробные части {x2}')
maximum = max(x2)
print(f'maximum = {maximum}')
minimum = min(x2)
print(f'minimum = {minimum}')
final_reply = round((maximum - minimum), 2)
print(f'ответ: {final_reply}')

