def single_loop(n):
    count = 0
    for i in range(n):
        count += 1
    print(f'Single loop ops: {count} => O(n)')


def nested_loop(n):
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    print(f'Nested loop ops: {count} => O(n^2)')


def triangular_loop(n):
    count = 0
    for i in range(n):
        for j in range(i):
            count += 1
    print(f'Triangular loop ops: {count} => O(n^2)')


def halving_loop(n):
    count = 0
    i = n
    while i > 1:
        i //= 2
        count += 1
    print(f'Halving loop ops: {count} => O(log n)')


def linear_search_cases(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            print(f'Found at index {i}')
            return i
    print('Not found')
    return -1


n = 8

single_loop(n)
nested_loop(n)
triangular_loop(n)
halving_loop(n)

arr = [1, 2, 3, 4, 5, 6, 7, 8]

print('--- Linear Search Cases ---')

print('Best case (target=1):', linear_search_cases(arr, 1))
print('Worst case (target=8):', linear_search_cases(arr, 8))
print('Not found (target=99):', linear_search_cases(arr, 99))