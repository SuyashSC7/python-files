a = [
    [2, -8, 4, 0],
    [-3, -1, 0],

]

n = len(a)

# Forward elimination (make below diagonal = 0)
for i in range(n):
    # Make diagonal 1
    diag = a[i][i]
    for j in range(i, len(a[0])):
        a[i][j] /= diag

    # Make below elements zero
    for k in range(i+1, n):
        factor = a[k][i]
        for j in range(i, len(a[0])):
            a[k][j] -= factor * a[i][j]

# Back substitution (make above diagonal = 0)
for i in range(n-1, -1, -1):
    for k in range(i-1, -1, -1):
        factor = a[k][i]
        for j in range(i, len(a[0])):
            a[k][j] -= factor * a[i][j]

# Final matrix
for row in a:
    print(row)
for i in range(n):
    print(f"x{i+1}= {a[i][n]}")