M = int(input("Enter the number of rows (M): "))
N = int(input("Enter the number of columns (N): "))

print("Enter elements for Matrix A:")
matrix_A = []
for i in range(M):
    row = []
    for j in range(N):
        element = int(input(f"Element [{i+1}][{j+1}]: "))
        row.append(element)
    matrix_A.append(row)

print("Enter elements for Matrix B:")
matrix_B = []
for i in range(M):
    row = []
    for j in range(N):
        element = int(input(f"Element [{i+1}][{j+1}]: "))
        row.append(element)
    matrix_B.append(row)

matrix_sum = []
for i in range(M):
    row = []
    for j in range(N):
        row.append(matrix_A[i][j] + matrix_B[i][j])
    matrix_sum.append(row)

print("Matrix Addition Result:")
for row in matrix_sum:
    print(row)

if M == N:
    matrix_product = []
    for i in range(M):
        row = []
        for j in range(N):
            product_sum = 0
            for k in range(N):
                product_sum += matrix_A[i][k] * matrix_B[k][j]
            row.append(product_sum)
        matrix_product.append(row)

    print("Matrix Multiplication Result:")
    for row in matrix_product:
        print(row)
else:
    print("Matrix multiplication is not possible for non-square matrices.")
