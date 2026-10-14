# 14 oct 2026 

# Create a NumPy array containing numbers from 1 to 10.
import numpy as np
arr = np.array([1,2,3,4,5])
print("NumPy array :",arr)

 # Create a 1D array containing 5 integers of your choice.
arr1 = np.array([1,2,3,4,4])
print("1D Array :",arr1)

 # Create a 2D array with 3 rows and 3 columns.
arr2 = np.array([[11,22,33],[44,55,66],[77,88,99]])
print("2D array with 3R 3C:", arr2)

 # Create an array of 5 zeros using NumPy.
arr = np.array([1,2,3,4,5])
zeros_array = np.zeros(5)
print("zeross",zeros_array)

 # Create an array containing numbers from 10 to 50 with a step of 10.
# arr = np.array([10,20,30,40,50])
print("linespace--",np.linspace(10,51,10))

 # Create an array containing 10 equally spaced numbers between 0 and 1.
arr =np.array([10,20,30,40,50])
print("===",np.linspace(0,10,1))

 # Create an dentity matrix of size 4 × 4.
arr = np.array([2,4])
print("dentity matrix",np.eye(4,4))


arr = np.linspace(0, 1, 10)

print("----",arr)