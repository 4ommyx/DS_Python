import numpy as np

# .shape : บอกถึงขนาดของ Matrix 
# .size  : บอกถึงจำนวนสมาชิกทุกตัวใน Matrix 
# .itemsize : บอกถึงขนาดของ สมาขิกแต่ละตัว 
# Ex int 4 byte / complex 16 byte (1 byte = 8 byte)
arr = [[1, 2, 3],[4, 5, 6]]
arr = np.array(arr)
print("array : ",arr)
print("shape of array : ",arr.shape)
print("size of array : ",arr.size)
print("itemSize : ",arr.itemsize)
print("-------------------------")
arr = np.array(arr, dtype=complex)
print("array : ",arr)
print("shape of array : ",arr.shape)
print("size of array : ",arr.size)
print("itemSize : ",arr.itemsize)
print("-------------------------")