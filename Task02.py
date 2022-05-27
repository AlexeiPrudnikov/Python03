import random
minValue = -10
maxValue = 10
def MultPairelements(intList):
    result = []
    if len(intList) % 2 == 1:
        count = len(intList) // 2 + 1
    else:
        count = len(intList) // 2
    for i in range(count):
        result.append(intList[i] * intList[len(intList)-i-1])
    return result
try:
    print('==========Задача № 2==========')
    print('Вывод произведения пар элементов последовательности')
    countElements = int(input('Введите длину последовательности: '))
    if countElements > 0:
        print(f'Производится генерация последовательности длины {countElements}...')
        intList = []
        for i in range(countElements):
            intList.append(random.randint(minValue, maxValue))
        print(intList)
        print('Произведения пар элементов последовательности...')
        print(MultPairelements(intList))
    else:
        print('Число элементов должно быть больше 0')
except ValueError:
    print('Введено не число')