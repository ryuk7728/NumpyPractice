import numpy as np

# #Basics
# a=np.array([1,2,3,4,5])
# print(a)

# #2D Array
# b=np.array([[1,2,3],[4,5,6]])
# print(b)

# #Specify Data Type
# c=np.array([1,2,3],dtype='int16')

# #Get Dimensions
# print(b.ndim)

# #Get Shape (Order of matrix)
# print(b.shape)

# #Get Type
# print(c.dtype)

# #Get the number of bytes per element
# print(c.itemsize)

# #Print number of elements
# print(b.size)

# #Print total number of bytes
# print(b.nbytes)

# #Get specific element
# print(b[0,1])

# #Get row
# print(b[1,:])

# #Change element
# b[1,1]=10
# print(b)

# #3D array
# d=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print(d.shape)

# #Create 0's matrix
# e=np.zeros((2,2,2))
# print(e)

# #Create 1's matrix
# f=np.ones((3,3,3))
# print(f)

# #Create a matrix with all numbers same
# g=np.full((2,2),55)
# print(g)

# #Create a matrix with random decimal numbers
# print(np.random.rand(3,4))

# #Create identity matrix
# print(np.identity(4))

# #Practice
# h=np.ones((5,5))
# h[1,1:4]=[0,0,0]
# h[2,1:4]=[0,9,0]
# h[3,1:4]=[0,0,0]
# print(h)

# #Be careful while copying arrays
# b=np.array([1,2,3],dtype='float64')
# a=b.copy()
# b[0]=100
# print(a)

# #Mathematics
# a+=2
# print(a)
# a-=2
# print(a)
# a*=2
# print(a)
# a/=2
# print(a)
# a**=2
# print(a)
# a=np.sin(a)
# print(a)

# #Linear Algebra
# a=np.full((2,3),1)
# print(a)
# b=np.full((3,2),2)
# print(b)

# #Matrix Multiplication
# c=np.matmul(a,b)
# print(c)

# #Determinant
# c=np.linalg.det(c)
# print(c)

# #Statistics
# stat=np.array([[1,2,3],[-1,5,6]])

# #Minimum
# print(np.min(stat))

# #Maximum
# print(np.max(stat))

# #Sum
# print(np.sum(stat))

# #Mean
# print(np.mean(stat))

#Reshape
a=np.array([1,2,3,4,5,6])
print("a: ",a.reshape(3,2))
print("a: ",a.reshape(2,-1)) #converts the array into 2 rows and it auto calculates the number of columns

