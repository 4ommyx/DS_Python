import numpy as np 

# create 0D array
arr0 = np.array(1)
print("0D array is : ",arr0)
# .ndim ระบุ Dimemtion of array (มิติของ array)
print("Dimension : ",arr0.ndim) 
print("-----------------------")

# create 1D array
arr1 = np.array([1,2,3,4,5])
print("1D array is : ",arr1)
print("Dimension : ",arr1.ndim)
lis = [1,2,3,4]
arr1 = np.array(lis)
print("1D array is : ",arr1)
print("Dimension : ",arr1.ndim)
print("-----------------------")

# create 2D, 3D array
arr2 = np.array([[1,2,3], [4,5,6], [7,8,9]])
print("2D array is : ",arr2)
print("Dimension : ",arr2.ndim)
print("-----------------------")
arr3 = np.array([[[1,2,3], [4,5,6], [7,8,9]]])
print("3D array is : ",arr3)
print("Dimension : ",arr3.ndim)
print("-----------------------")