first_day = int(input('Введите количество километров, которые спортсмен пробежал в первый день: '))
last_day = int(input('Введите количество километров, которые спортсмен пробежал в последний день: '))
current_day = first_day
i = 1
print(f'1-ый день: {first_day}')
while current_day < last_day:
    current_day = current_day * 1.1
    print(f'{i+1}-ый день: {round(current_day, 2)}')
    i += 1
print(f'Ответ: на {i}-й день спортсмен достиг результата — не менее {last_day} км. ')
