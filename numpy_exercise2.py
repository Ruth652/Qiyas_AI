import numpy as np

a = np.array([1, 2, 3])
print(a.dtype)

a2 = np.array([1.5, 2.5, 3.5])
print(a2.dtype)

str_ = np.array(["r", "b"])
print(str_.dtype)

a_int = np.array([1,2, 3], dtype = np.int32)
print(a_int.dtype)

a_float = np.array([1,2, 3], dtype = np.float64)
print(a_float.dtype)
print( "Memory Location:", a_float.nbytes)

print("Array shape:", a_float.shape)
print("Array size:", a_float.size)

# Numpy Mathematical
a1 = np.arange(1,5)
a2 = np.arange(6,10)

print("sum of a1 and a2:", a1 + a2)
print("subtraction of a1 and a2:", a1 - a2)
print("sqrt of a1:", np.sqrt(a1)) # a1.sqrt()
print("variance of a1:", np.var(a1)) # a1.var()

b = np.array([[1,2,3],
[3,4,5]
])
c = np.array([[1,2,3],
[3,4,5]
])
print("matrix addition:", b + c )

A = np.array([[1, 2],
             [3, 4]]
)

B = np.array([[5, 6],
             [7, 8]]
)
print("matix multiplication:", np.dot(A,B))
print("matrix transpose:", np.transpose(b)) # b.T(), np.T(b)

