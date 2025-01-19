def is_prime(func):
    def wrapper(*args, **kwargs):
        n = func(*args, **kwargs)
        if n < 2:
            result = f'{n} - не простое и не сложное число'
        elif n == 2:
            result = f'{n} - Простое число'
        else:
            f = n ** (1/2)
            k = int(f + 1)
            lst = range(2, k)
            for i in range(2, k):
                if n % i == 0:
                    result = 'Составное число'
                else:
                    result = 'Простое число'
        print(result)
        return n
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)