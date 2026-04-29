def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0

    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1

    return comparisons, swaps


arr1 = [64, 34, 25, 12, 22, 11, 90]
arr2 = sorted(arr1)

print("Original:", arr1)

c, s = bubble_sort(arr1)
print("Sorted:", arr1)
print("Comparisons:", c, "Swaps:", s)

print("\nAlready sorted input:")
c2, s2 = bubble_sort(arr2)
print("Sorted:", arr2)
print("Comparisons:", c2, "Swaps:", s2)