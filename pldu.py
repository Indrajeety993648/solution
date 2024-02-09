def partial_pivoting(U, P, j):
    n = len(U)

    pivot = j
    for k in range(j + 1, n):
        if abs(U[k][j]) > abs(U[pivot][j]):
            pivot = k

    if pivot != j:
        U[j], U[pivot] = U[pivot], U[j]
        P[j], P[pivot] = P[pivot], P[j]

def lu_decomposition(U, n):
    L = [[0] * n for _ in range(n)]
    D = [0] * n

    for j in range(n):
        # Compute L, D, U
        L[j][j] = 1
        D[j] = U[j][j]
        for i in range(j + 1, n):
            factor = U[i][j] / U[j][j]
            L[i][j] = factor
            for k in range(j, n):
                U[i][k] -= factor * U[j][k]

    return L, D

def pldu(M):
    n = len(M)
    P = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    U = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            U[i][j] = M[i][j]
    
    for j in range(n):
        partial_pivoting(U, P, j)

        if U[j][j] == 0:
            return None  
    L, D = lu_decomposition(U, n)
    
    return P, L, D, U

# example for calculation...
M = [
    [2, 4, 1],
    [4, 9, 2],
    [1, 2, 3]
]

PLDU = pldu(M)
if PLDU:
    P, L, D, U = PLDU
    print("permutation matrix:")
    for row in P:
        print(row)

    print("Lower matrix:")
    for row in L:
        print(row)

    print("diagonal matrix:")
    print(D)

    print("upper triangular matrix:")
    for row in U:
        print(row)
else:
    print("matrix is singular matrix, no pldu decomposition possible")
