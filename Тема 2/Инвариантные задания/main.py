# Task
# Разработать функцию, возвращающую элементы ряда
# Фибоначчи по данному максимальному значению.

# реализация

def fibonac_v1(n):
    if n > 0:
        if n == 1:
            print('[0]')
        elif n > 1:
            res = [0] * n
            res[1] = 1
            for i in range(2, n):
                res[i] = res[i - 1] + res[i - 2]
            return res
    else:
        print('Число должно быть целым и положительным!')

def fibonac_v2(n):
    if n > 0:
        if n == 1:
            print('[0]')
        elif n > 1:
            res = [0, 1, ]
            for i in range(2, n):
                res.append(res[i - 1] + res[i - 2])
            return res
    else:
        print('Число должно быть целым и положительным!')


def fibonac_generator():  # генератор - итератор
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def fibonac_iterator(n):
    it = iter(list(range(2, n)))
    res = [0, 1, ]
    while True:
        try:
            x = next(it)
        except StopIteration:
            break
        res.append(res[x - 1] + res[x - 2])
    return res

if __name__ == "__main__":
    n = int(input('Введите число элементов: '))
    print(f'fibonac_v1({n}): \n', fibonac_v1(n))
    print(f'fibonac_v2({n}): \n', fibonac_v2(n))
    print(f'fibonac_iterator({n}): \n', fibonac_iterator(n))
    f = fibonac_generator()
    result = []

    assert n >= 0
    
    for x in range(n):
        result.append(f.__next__())
    print('Ряд Фибоначчи (итератор v2): \n', result)

    assert  n >= 0

