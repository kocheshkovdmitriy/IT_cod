from math import sqrt

def analiz(num: int):
    if n <= 1:
        return 'Простыми числами являются только натуральные больше 1'
    for dev in range(2, int(sqrt(abs(num)) + 1)):
        if num % dev == 0:
            return 'Составное'
    return 'Простое'

if __name__ == "__main__":
    n = int(input('Введиет натуральное число больше единицы: '))
    print(analiz(n))
