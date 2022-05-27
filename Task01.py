import random
minValue = -100
maxValue = 100
def SummOddElements(intList):
    summ = 0
    for i in range(1,len(intList), 2):
        summ += intList[i]
    return summ
try:
    print('==========Задача № 1==========')
    print('Вывод суммы элементов последовательности на нечетных позициях')
    countElements = int(input('Введите длину последовательности: '))
    if countElements > 0:
        print(f'Производится генерация последовательности длины {countElements}...')
        intList = []
        for i in range(countElements):
            intList.append(random.randint(minValue, maxValue))
        print(intList)
        print(f'Сумма элементов последовательности на нечетных позициях -> {SummOddElements(intList)}')
    else:
        print('Число элементов должно быть больше 0')
except ValueError:
    print('Введено не число')