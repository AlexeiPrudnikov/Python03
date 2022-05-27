def Negafibonachi(n):
    result = []
    result.append(0)
    if n == 0: return result
    result.append(1)
    for i in range(2, n + 1):
        result.append(result[i - 1] + result[i - 2])
    for i in range(n):
        result.insert(0, result[1] - result[0])
    return result
try:
    print('==========Задача № 5==========')
    print('Вывод последовательности негафибоначи длины N')
    n = int(input('Введите длину последовательности: '))
    if n > 0:
        print(Negafibonachi(n))
    else:
        print('Число элементов должно быть больше 0')
except ValueError:
    print('Введено не число')