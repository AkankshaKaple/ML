# 1. Write a python program to add below matrices

Matrix_1 = [[12, 7, 3],
            [4,5,6],
            [7,8,9]]
Matrix_2 = [[5, 8, 1],
            [6,7,3],
            [4,5,9]]

Resultant_Matrix = [[0, 0, 0],
                    [0,0,0],
                    [0,0,0]]
# Matrix= []
for index_1 in range(len(Matrix_1)):
    for index_2 in range(len(Matrix_1[0])):
        Resultant_Matrix[index_1][index_2] = Matrix_1[index_1][index_2] + Matrix_2[index_1][index_2]

print(Resultant_Matrix)
