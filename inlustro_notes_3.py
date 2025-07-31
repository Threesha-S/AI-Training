# scalar, vector, linear algebra
# ATS score

# scalar -> x = 4
# vector -> x = [2, 3, 4, 5, 7]       one-dimensional data
# matrix -> x = [[2, 3], [4, 5], [6, 7]]      two-dimensional data
# tensor

# numpy - numerical python -> to do mathematical calculation
# pytorch -

# import numpy as np
# scalar = 5
# vector = np.array([1, 2, 3, 4, 5, 6, 7])
# matrix = np.matrix([[1, 2], [3, 4]])
# print(scalar)
# print(vector.shape)         # display the number of columns
# print(matrix.shape)
# print(vector.ndim)          # display the dimension
# print(matrix.ndim)

# import numpy as np
# scalar = 5
# vector = np.array([1, 2, 3, 4, 5, 6])
# matrix = np.matrix([[1, 2, 3], [5, 6, 7], [9, 9, 0], [2, 3, 4]])
# print(scalar)
# print(vector.shape)
# print(np.linalg.matrix_rank(matrix))        # to find rank of a matrix

# import numpy as np
# row_wise = np.array([1, 2, 3])
# col_wise = np.array([[1], [2], [3]])
# print(row_wise)
# print(col_wise)
# print(row_wise.ndim)
# print(col_wise.shape)

# import numpy as np
# v1 = np.array([[1, 2], [3, 4]])
# v2 = np.array([[1, 2], [3, 4]])
# print(v1 * v2)
# print(2 * v1)

# import numpy as np
# v1 = np.array([[1, 2], [3, 4]])
# v2 = np.array([[1, 2], [3,4]])
# print(np.dot(v1, v2))
# print(v1 * v2)

# import numpy as np
# v1 = np.array([[1, 2, 3], [7, 9, 6]])
# v2 = np.array([[4, 5, 6], [9, 5, 6]])
# cross = np.cross(v1, v2)
# print(cross)

# import numpy as np
# A = [1, 2, 3]
# B = [4, 5, 6]
# v1 = np.array(A)
# v2 = np.array(B)
# print(np.dot(v1, v2))

# A = [1, 2, 3]
# B = [4, 5, 6]
# result = 0
# for i in range(len(A)):
#     result += A[i] * B[i]
# print(result)

A = [[1, 2, 3], [4, 5, 6]]
rows = len(A)
cols = len(A[0])
T = []
for j in range(cols):
    new_row = []
    for i in range(rows):
        new_row.append(A[i][j])
    T.append(new_row)
print('Transpose: ')
print(T)
# # Doubts: -
