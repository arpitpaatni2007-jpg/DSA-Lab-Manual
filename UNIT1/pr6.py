def binary_search(arr, key, low, high):

    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid

    elif arr[mid] > key:
        return binary_search(arr, key, low, mid - 1)

    else:
        return binary_search(arr, key, mid + 1, high)


arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

print('Array:', arr)
print()

test_keys = [23, 72, 1, 91, 2]

for key in test_keys:
    result = binary_search(arr, key, 0, len(arr) - 1)

    if result != -1:
        print(f'Key {key}: Found at index {result}')
    else:
        print(f'Key {key}: Not Found')


# Edge case: empty list
print('Empty list search:', binary_search([], 5, 0, -1))