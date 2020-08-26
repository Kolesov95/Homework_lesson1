user_number = input('Введите целое число: ')
i = 0
max_number = 0
while i != len(user_number):
    if int(user_number[i]) > int(max_number):
        max_number = user_number[i]
    i = i + 1
print(f'Наибольшая цифра: {max_number}')


