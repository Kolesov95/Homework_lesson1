user_number = (input('Введите число от 1 до 9: '))
if int(user_number) > 0 and (int(user_number) < 10):
    second_number = user_number*2
    third_number = user_number*3
    result = int(user_number)+int(second_number)+int(third_number)
    print(f'{user_number}+{second_number}+{third_number}={result}')
else:
    print('Некорректное число')

