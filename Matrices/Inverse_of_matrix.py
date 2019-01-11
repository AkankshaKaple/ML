# 5. Write a program to find inverse matrix of matrix X in problem 1		.


def minor_elements(m, i, j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]


def deternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant = determinant + ((-1)**c) * m[0][c] * deternminant(minor_elements(m, 0, c))
    return determinant


def inverse(Matrix):
    cofactor = []
    for i in range(len(Matrix)):
        list_cof = []
        for j in range(len(Matrix)):
            minors = minor_elements(Matrix, i, j)
            list_cof.append((-1) ** j * deternminant(minors))
        cofactor.append(list_cof)

    # print(cofactor)
    return cofactor


Matrix = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]
det = deternminant(Matrix)
print(det)
inverse = inverse(Matrix)
print(inverse)

print("inverse = ", inverse, "* 1/", det)