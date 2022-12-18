# 3. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

user_number = float(input('Enter your number: '))

if (user_number % 5 == 0 and user_number % 10 == 0 or user_number % 15 == 0) and user_number % 30 != 0:
    print('Your number is nice')
else:
    print('Try again')
variable.