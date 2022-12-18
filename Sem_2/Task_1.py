# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
    
#     *Пример:*
    
#     - Для N = 5: 1, -3, 9, -27, 81


# import random
# n = int(input('Enter N: '))
# for i in range (n):
#     print(random.randint(0,10), end=' ')

# or

import random
num = 5
a = []
for i in range (num):
    a.append(random.randint(-10,10), end = ' ')
print(a)
