import numpy as np
print(np.__version__) #check the version of numpy

# array
# one dimensional array
arr = np.array([10,20,30,40])
print(arr)
print(type(arr))

# two dimensional array
arr2 = ([[1,2,3],[4,5,6]]) 
print(arr2)

# three dim array
arr3 =([[1,2],[3,4],[5,6],[7,8]])
print (arr3)

# array attributes
arr = np.array([[1,2,6],[3,4,6]])
print (arr.ndim) #  print numbers of dimensinal 
print(arr.shape) # return Row2 & Col3
print(arr.size) # size  written total number of element in the array
print(type(arr))
print(arr.dtype)
print(np.zeros((2,3))) # return 0 
print(np.ones((2,3))) 
print(np.full((2,3),5)) # as we want the data to be print 
print(np.arange(1,10,2)) 
print(np.linspace(0,10,5)) 

# startval = 0
# stopval = 10
# numofval = 5

# 10-0 = 10
# 5-1 = 4 
# 4 dvide 10 = 2.5
print(np.eye(3,4)) #(4)
print(np.random.randint(100))


marks = np.array([70,90,80,60,100])
print(np.sum(marks))
print("min:",np.min(marks))
print(np.max(marks))
print("mean",np.mean(marks)) 
print("median:",np.median(marks))
print(np.std(marks)) 
# standard division formulla


 



 
