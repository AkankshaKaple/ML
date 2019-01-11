# 6. Write a program to find transpose matrix of matrix Y in problem 1

Matrix_1 = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]

Matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(len(Matrix_1)):
    for j in range(len(Matrix_1[i])):
        Matrix[j][i] = Matrix_1[i][j]
print(Matrix)
