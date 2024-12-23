import numpy as np

# Matrices define:
A = np.array([[4, 3], [2, 1]])
B = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
C = np.array([[2, 1], [5, 3]])
D = np.array([[1, 0, 2], [0, 1, 3], [4, 5, 6]])
E = np.array([[3, 0, 2], [2, 0, -2], [0, 1, 1]])

# Determinants
det_A = np.linalg.det(A)
det_B = np.linalg.det(B)
det_D = np.linalg.det(D)
det_E = np.linalg.det(E)

# Inverse
inv_A = np.linalg.inv(A) if det_A != 0 else "Not invertible"
inv_C = np.linalg.inv(C) if np.linalg.det(C) != 0 else "Not invertible"
inv_E = np.linalg.inv(E) if det_E != 0 else "Not invertible"

# Show Results
print("Determinant of A:", det_A)
print("Determinant of B:", det_B)
print("Inverse of A:\n", inv_A)
print("Inverse of C:\n", inv_C)
print("Determinant of E:", det_E)
print("Inverse of E:\n", inv_E)
