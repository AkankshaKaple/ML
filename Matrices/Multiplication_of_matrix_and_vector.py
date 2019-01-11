# 3. Write a program to perform multiplication of given matrix and vector
# X = [[ 5, 1 ,3], [ 1, 1 ,1], [ 1, 2 ,1]], Y = [1, 2, 3]

Matrix_1 = [[5, 1, 3], [1, 1, 1], [1, 2, 1]]
Row_Matrix = [1, 2, 3]
Resultant_Matrix = [0,0,0]


for row_index in range(len(Row_Matrix)):
    value = 0
    for column_index in range(len(Matrix_1[row_index])):
        value = Matrix_1[column_index][row_index] * Row_Matrix[column_index] + value
        # print(val)
    Resultant_Matrix[row_index] = value
print(Resultant_Matrix)