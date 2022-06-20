def say_hi(n=5):
    if n == 0:
        return
    print("Hi")
    say_hi(n-1)


# say_hi()


def recursive_power(num, power):
    if power == 0:
        return 1
    return num * recursive_power(num, power - 1)


# print(recursive_power(2, 5))

def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

# The function above is uneffcient and slow.
#for n in range(1, 101):
#    print(n, ":", fibonacci(n))

# We need to use memoization - return of cached values


fibonacci_cache = {}


def fibonacci(n):
    # if we have cached the value then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # compute the Nth term
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        value =  fibonacci(n-1) + fibonacci(n-2)

    fibonacci_cache[n] = value
    return value


for n in range(1, 100001):
    print(n, ":", fibonacci(n))

