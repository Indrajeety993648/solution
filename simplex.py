def pivot(table, row, col):
    pivotvalue = table[row][col]
    num_rows, num_cols = len(table), len(table[0])

    for j in range(num_cols):
        table[row][j] /= pivotvalue

    for i in range(num_rows):
        if i != row:
            multiplier = table[i][col]
            for j in range(num_cols):
                table[i][j] -= multiplier * table[row][j]

def findingpivotcoloum(table):
    num_cols = len(table[0]) - 1
    pivot_col = min(range(num_cols), key=lambda j: table[-1][j])
    if table[-1][pivot_col] >= 0:
        return -1
    return pivot_col

def findingpivotrow(table, pivot_col):
    num_rows = len(table) - 1
    ratios = [float('inf')] * num_rows
    for i in range(num_rows):
        if table[i][pivot_col] > 0:
            ratios[i] = table[i][-1] / table[i][pivot_col]
    pivot_row = min(range(num_rows), key=lambda i: ratios[i])
    if ratios[pivot_row] == float('inf'):
        return -1  
    return pivot_row

def simplexmethod(A, b, c):
    m, n = len(A), len(A[0])
    table = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m):
        table[i][:n] = A[i]
    for i in range(m):
        table[i][-1] = b[i]
    table[-1][:n] = [-ci for ci in c]

    while True:
        pivot_col = findingpivotcoloum(table)
        if pivot_col == -1:
            break
        pivot_row = findingpivotrow(table, pivot_col)
        if pivot_row == -1:
            return None 
        pivot(table, pivot_row, pivot_col)

    solution = [0] * n
    for j in range(n):
        column = [table[i][j] for i in range(m)]
        if column.count(0) == m - 1 and column.count(1) == 1:
            solution[j] = table[column.index(1)][-1]

    return solution

# Example usage:
A = [
    [3, 5,6],
    [1,1,1],
    [1,1,2]
]
b = [1000, 200,280]
c = [50,100,150]

solution = simplexmethod(A, b, c)
print("Solution:", solution)
