# 3. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.

# string1 = input('Type text: ')
# string2 = input('What are u looking for? ')

# print(string1.count(string2))

# or

first_str = input('Введите исходную строку: ')
second_str = input('Введите строку: ')
count = 0
for i in range(len(first_str) - len(second_str)):
    if first_str[i] == second_str[0]:
        flag = True
        for j in range(1,len(second_str)):
            if second_str[j] != first_str[i+j]:
                flag = False
        if flag:
            count += 1
print(count)