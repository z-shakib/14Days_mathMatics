import numpy as np

# Example system: A * X = B
A = np.array([[1, 1, 1], [2, 3, 4], [3, 2, 1]])
B = np.array([6, 20, 14])

# 1. Solve using Row Reduction (NumPy built-in)
solution_row = np.linalg.solve(A, B)

# 2. Solve using Matrix Inverse (if possible)
if np.linalg.det(A) != 0:  # Check if determinant is non-zero
    A_inv = np.linalg.inv(A)
    solution_inv = np.dot(A_inv, B)
else:
    solution_inv = "Matrix is singular, no inverse"

# 3. Check Rank of Matrix
rank_A = np.linalg.matrix_rank(A)

# Print Results
print("Solution using Row Reduction:", solution_row)
print("Solution using Matrix Inverse:", solution_inv)
print("Rank of Matrix A:", rank_A)
