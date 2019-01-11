# 2. Write a program to perform scalar multiplication of matrix and a number

Matrix_1 = [[12, 7, 3],
            [4, 5, 6],
            [7, 8, 9]]
Scalar_value = 9
Matrix = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for row_index in range(len(Matrix_1)):
    for column_index in range(len(Matrix_1[row_index])):
        Matrix[row_index][column_index] = Scalar_value * Matrix_1[row_index][column_index]

print(Matrix)
