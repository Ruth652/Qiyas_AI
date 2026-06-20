# one of the most important libraries for scientific computing

import numpy as np

# numpy arrays are more efficient(faster, uses less memory) than lists for numerical operations
# numbers = np.array([1,2,3,4,5])
# print(numbers * 2)

# # 2d arrays
# arr = np.array([
#     [1,2,3],
#     [4,5,6]
# ])

# arr_zeros = np.zeros((2,3)) # creates a 2x3 array filled with zeros
# print(arr_zeros)

# arr_ones = np.ones(4) # creates a 1d array of length 4 filled with ones

# # arange() creates an array with a range of values
# arr_range = np.arange(1, 20)
# print(arr_range)

# # linspace() creates an array of evenly spaced values between a start and end point
# arr_linspace = np.linspace(0, 10, 5) # creates an array of 5 evenly spaced values between 0 and 10
# print(arr_linspace)

# '''
# array operations
# '''

# a = np.array([1,2,3])
# b = np.array([4,5,6])

# print(a + b)
# print(a * b)
# print(a / b)
# print(a - b)

# scalar operations
# print(a + 10) # adds 10 to each element in the array
'''
data types
int32, int64, float32, float64, bool, complex
'''

# c = np.array([1,2,3])
# print(c.dtype) # int64 
# # explicitly specify data type
# d = np.array([1,2,3], dtype=np.int32)

# e = np.array([1,2,4], dtype = np.float64)
# f = np.array(["AAU", "qiyas"], dtype='U10')

# # using np.dtype() 
# dt = np.dtype(np.int32)
# print(dt) 

# # math operations
# g = np.array([1,2,3], dtype = np.float64)

# print(np.sum(g))
# print(np.mean(g))
# print(np.median(g))
# print(np.min(g))
# print(np.sqrt(g))
# print(np.power(g, 2))
# print(np.std(g)) # standard deviation






# '''''
# Exercise
# 1.create a NumPy array containing the first 10 natural numbers.
# 2.find the dataype
# 3.Add two arrays
# 4. find the average
# '''
# new_arr = np.arange(1, 11)
# print(new_arr)
# print("dataype of new_arr:", new_arr.dtype)

# arr2 = np.arange(11, 21)
# print(new_arr + arr2)

# print("average of new_arr:", np.mean(new_arr))



'''
new_section
'''

arr3 = np.array([[1,2,3], [4,5,6]])
print(arr3.shape) # 2, 3  - row , column
print(arr3.ndim) # 1 - ndim - number of dimensions
print(arr3.size) # 6 - the total number of elements in the array

# numpy indexing and slicing

sales = np.array([
    [100, 200, 300],
    [150, 250, 350],
    [200, 300, 400]
])
print(sales[:,0]) # all rows, first column
print(sales[:2]) # all columns, first two rows ( start at 0 and end at 2, exclusive)
print(sales[:,1:]) # all rows, columns from index 1 to the end ( start at 1 and end at the end of the array)
print(sales[:]) # all rows, all columns 




