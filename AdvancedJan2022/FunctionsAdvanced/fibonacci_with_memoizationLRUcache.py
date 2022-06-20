from functools import lru_cache


@lru_cache(maxsize=1000)
def fibonacci(n):
    if type(n) != int:
        raise TypeError("n must be a positive integer")
    if n < 1:
        raise ValueError("n must a positive integer")

    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)


# print(fibonacci(0))

