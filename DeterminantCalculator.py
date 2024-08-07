def calculatedeterminant(matrixgiven):
    if len(matrixgiven) != len(matrixgiven[0]):
        return 0
    if len(matrixgiven) == 1:
        return matrixgiven[0][0]
    if len(matrixgiven) == 2:
        return matrixgiven[0][0] * matrixgiven[1][1] - matrixgiven[0][1] * matrixgiven[1][0]
    
    count = 0
    for i in range(len(matrixgiven)):
        submatrix = []
        for j in range(0, len(matrixgiven) - 1):
            subrow = []
            for k in range(len(matrixgiven)):
                if k != i:
                    subrow.append(matrixgiven[j + 1][k])
            submatrix.append(subrow)
        cofactor = (-1) ** i * calculatedeterminant(submatrix) * matrixgiven[0][i]
        count += cofactor
    return count


rows = int(input("Enter the number of rows in the matrix: "))
cols = int(input("Enter the number of columns in the matrix: "))

userinputmatrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        element = float(input(f"Enter element at position ({i+1}, {j+1}): "))
        row.append(element)
    userinputmatrix.append(row)

result = calculatedeterminant(userinputmatrix)
print(f"The determinant of the matrix is: {result}")