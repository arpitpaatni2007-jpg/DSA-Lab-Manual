def insert_at(arr, pos, val):
    shifts = len(arr) - pos
    arr.insert(pos, val)
    return shifts


def delete_at(arr, pos):
    shifts = len(arr) - pos - 1
    removed = arr.pop(pos)
    return removed, shifts


arr = [10, 20, 30, 40, 50]

print("Original array:", arr)

# Insert operations
shifts = insert_at(arr, 0, 5)
print("\nInsert at start:", arr, "| shifts:", shifts)

shifts = insert_at(arr, 3, 25)
print("Insert in middle:", arr, "| shifts:", shifts)

shifts = insert_at(arr, len(arr), 60)
print("Insert at end:", arr, "| shifts:", shifts)


# Delete operations
removed, shifts = delete_at(arr, 0)
print("\nDelete from start:", arr, "| removed:", removed, "| shifts:", shifts)

removed, shifts = delete_at(arr, 2)
print("Delete from middle:", arr, "| removed:", removed, "| shifts:", shifts)

removed, shifts = delete_at(arr, len(arr) - 1)
print("Delete from end:", arr, "| removed:", removed, "| shifts:", shifts)