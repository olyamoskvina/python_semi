# 3. Задайте два числа.
# # Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

# ==  Решение задачи №3 (просто перебором всех чисел)== 

a = int(input('введи А: '))
b = int(input('введи B: '))

max_num = max(a,b)

 # ранж от .. до ПРЕДЕЛА (шаг убран)
for i in range(max_num, (a*b)+1):

    if i % a == 0 and i % b == 0:
        print(f'НОК: {i}')

        break



# == Решение задачи №3 (просто перебором всех чисел)== 

a = int(input('введи А: '))
b = int(input('введи B: '))

max_num = max(a,b)

# ранж от .. до ПРЕДЕЛА (шаг указан)
for i in range(max_num, (a*b)+1, max_num): 
    if i % a == 0 and i % b == 0:
        print(f'НОК: {i}')
        break