gain = int(input('Введите значение выручки фирмы: '))
costs = int(input('Введите издержки фирмы: '))
if costs > gain:
    print('Фирма терпит убытки')
elif costs == gain:
    print('Фирма отработала в ноль')
elif gain > costs:
    income = gain - costs
    rent = (income / gain) * 100
    print(f'Фирма отработала с прибылью. Прибыль: {income}. Рентабельность: {rent}%')
    employees = int(input('Введите количество сотрудников: '))
    print(f'Прибыль на одного сотрудника: {income / employees}')
