import numpy as np 

matrix = np.random.randint(1,11,size=(3,3))
print("original matrix\n", matrix)

rank = np.linalg.matrix_rank(matrix)
print("\nRank of the matrix : ", rank)