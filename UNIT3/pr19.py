import random
import time


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

def time_function(func, arr):
    start = time.time()
    if func == merge_sort or func == quick_sort:
        func(arr.copy())
    else:
        temp = arr.copy()
        func(temp)
    end = time.time()
    return round(end - start, 5)


sizes = [1000, 5000, 10000]

for size in sizes:
    print(f"\nDataset size: {size}")

    random_data = [random.randint(1, 10000) for _ in range(size)]
    sorted_data = sorted(random_data)
    reverse_data = sorted(random_data, reverse=True)

    print("Insertion Sort:")
    print("  Random:", time_function(insertion_sort, random_data))
    print("  Sorted:", time_function(insertion_sort, sorted_data))
    print("  Reverse:", time_function(insertion_sort, reverse_data))

    print("Merge Sort:")
    print("  Random:", time_function(merge_sort, random_data))
    print("  Sorted:", time_function(merge_sort, sorted_data))
    print("  Reverse:", time_function(merge_sort, reverse_data))

    print("Quick Sort:")
    print("  Random:", time_function(quick_sort, random_data))
    print("  Sorted:", time_function(quick_sort, sorted_data))
    print("  Reverse:", time_function(quick_sort, reverse_data))