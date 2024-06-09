from functions import square_adjacency_matrix, count_grid_routes
from numpy.linalg import matrix_power

# ADJACENCY MATRIX:

# Parameters
L = 21 # lattice length -> vertex-based, not site-based
N = L**2 # number of vertices
r = 2*(L-1) # path length
first = 0 # first vertex
last = int(N-1) # last vertex

matrix = square_adjacency_matrix(L)
exp_matrix = matrix_power(matrix,r)
print(int(exp_matrix[first][last]))


# COMBINATORICS:

n = 20
print(int(round(count_grid_routes(n))))