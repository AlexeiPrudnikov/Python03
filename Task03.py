import random
import math
minValue = -100
maxValue = 100
def MaxMinDiffFrac(floatList):
    if len(floatList) == 1: return 0
    minFrac = 1
    maxFrac = 0
    for i in floatList:
        temp = abs(i)
        if (temp % 1 > maxFrac):
            maxFrac = temp % 1
        if (temp % 1 < minFrac):
            minFrac = temp % 1
    return round(maxFrac - minFrac, 2)
try:
    print('==========Задача № 3==========')
    print('Вывод разницы между максимальным и минимальным значением дробной части')
    countElements = int(input('Введите длину последовательности: '))
    if countElements > 0:
        print(f'Производится генерация последовательности длины {countElements}...')
        floatList = []
        for i in range(countElements):
            floatList.append(round(random.uniform(minValue, maxValue), 2))
        print(floatList)
        print(f'Разница между максимальным и минимальным значением дробной части элементов -> {MaxMinDiffFrac(floatList)}')
    else:
        print('Число элементов должно быть больше 0')
except ValueError:
    print('Введено не число')
