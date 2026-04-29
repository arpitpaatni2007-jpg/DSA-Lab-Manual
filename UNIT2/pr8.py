def row_sum(matrix):
    for i in range(len(matrix)):
        print(f"Row {i} sum:", sum(matrix[i]))


def col_sum(matrix):
    cols = len(matrix[0])
    for j in range(cols):
        s = 0
        for i in range(len(matrix)):
            s += matrix[i][j]
        print(f"Column {j} sum:", s)


def search(matrix, key):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == key:
                return (i, j)
    return None


def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(matrix[i][j])
        result.append(row)
    return result


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    print(row)

print("\nRow sums:")
row_sum(matrix)

print("\nColumn sums:")
col_sum(matrix)

key = 5
pos = search(matrix, key)
print(f"\nSearch {key}:", pos if pos else "Not Found")

print("\nTranspose:")
t = transpose(matrix)
for row in t:
    print(row)