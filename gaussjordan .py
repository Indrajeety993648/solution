def swapping(A, i, k):
    A[i], A[k] = A[k], A[i]

def forward(A, B):
    n = len(A)

    for cols in range(n):
        maxrow = cols
        for i in range(cols + 1, n):
            if abs(A[i][cols]) > abs(A[maxrow][cols]):
                maxrow = i
        swapping(A, cols, maxrow)
        swapping(B, cols, maxrow)
        for i in range(cols + 1, n):
            factor = A[i][cols] / A[cols][cols]
            for k in range(cols, n):
                A[i][k] -= factor * A[cols][k]
            B[i] -= factor * B[cols]

def againsuBstituting(A, B):
    n = len(A)
    x = [0] * n

    for i in range(n - 1, -1, -1):
        x[i] = B[i] / A[i][i]
        for k in range(i):
            B[k] -= A[k][i] * x[i]

    return x

def solve(A, B):
    m, n = len(A), len(A[0])

    if m != n:
        return -1  
    aug_matrix = [row[:] + [B[i]] for i, row in enumerate(A)]

    forward(aug_matrix, B)
    for i in range(n):
        if all(A[i][k] == 0 for k in range(n)) and B[i] != 0:
            return -1  
    return againsuBstituting(aug_matrix, B)

def det(A):
    n = len(A)
    if n != len(A[0]):
        return 0  
    if n == 1:
        return A[0][0]

    determinant = 0
    sign = 1

    for k in range(n):
        suBmatrix = [row[:k] + row[k + 1:] for row in A[1:]]
        determinant += sign * A[0][k] * det(suBmatrix)
        sign *= -1

    return determinant

# example to calculate the function
A = [
    [2,1,2],
    [1,2,1],
    [3,1,-1]
]
B = [10,8,2]

print("calculated determinant:",det(A))
print("Answer:",solve(A, B))
