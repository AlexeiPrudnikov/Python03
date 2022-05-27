def DecToBin(n):
    div = n
    mod = 0
    binNumber = []
    if n > 1:
        while (div > 0):
            binNumber.append(div % 2)
            div = div // 2
    else:
        binNumber.append(n)
    binNumber.reverse()
    return ''.join(map(str, binNumber))
try:
    print('==========Задача № 4==========')
    print('Перевод делятичного числа в двоичное')
    n = int(input('Введите неотрицательное число: '))
    if n >= 0:
        print(f'Число {n} = {DecToBin(n)}')
    else:
        print('Число элементов должно быть больше 0')
except ValueError:
    print('Введено не число')