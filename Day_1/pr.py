import numpy as np
#! Matrices:
A = np.array([[1,2], [3,4]])
B = np.array([[5,6], [7,8]])

#! Add the matrices:
addition = A + B
#! Subtract B - A:
sub = B - A
#! Scaler Multiplication:
k = -2
multy = k*A
#! Matrices Multiplication:
matMulti = np.dot(A, B)
#! Transpose:
trans = np.transpose(A)

print(addition)
print(sub)
print(multy)
print(matMulti)
print(trans)

