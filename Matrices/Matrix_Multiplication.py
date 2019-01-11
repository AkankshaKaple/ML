# 4. Write a program to multiply matrices in problem 1

Matrix_1 = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]
Matrix_2 = [[5, 8, 1], [6, 7, 3], [4, 5, 9]]

# print(len(Matrix_1))

Resultant_Matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# for k in range(len(Matrix_2) * len(Matrix_1)):
for k in range(len(Matrix_2)):
    for i in range(len(Matrix_2)):
        value = 0
        for j in range(len(Matrix_2)):
            value = Matrix_1[j][i] * Matrix_2[k][j] + value
        # print(value)
        Resultant_Matrix[k][i] = value

print(Resultant_Matrix)