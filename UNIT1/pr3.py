def factorial(n):

    if n < 0:
        print('Error: factorial not defined for negative numbers.')
        return None

    if n == 0:
        return 1

    return n * factorial(n - 1)


print('factorial(0) =', factorial(0))
print('factorial(1) =', factorial(1))
print('factorial(4) =', factorial(4))
print('factorial(7) =', factorial(7))
print('factorial(-1) =', factorial(-1))