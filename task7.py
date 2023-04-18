def fib(n: int):
    """
    На всякий случай, нумерация чисел Фиббоначи начинается с 0
    что бы не возникло недопонимания
    """
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    n = int(input())
    print(fib(n))