import numpy as np
# การ slice array [] : ใช้หลักการ [start, stop, step] 
# -[:n] : slice ตั้งแต่เริ่มต้นถึงตัวที่ n-1 
# -[n:] : slice ตั้งแต่ตัวที่ n ถึงตัวสุดท้าย
a0 = np.arange(10)
print("Original : {}".format(a0))
print("Slice : {}".format(a0[:5]))
print("Slice : {}".format(a0[5:]))
print("Slice : {}".format(a0[:7:2]))
print("----------------------")
a1 = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print("Slice : {}".format(a1[:2]))
print("Slice : {}".format(a1[:2,:2]))
print("Slice : {}".format(a1[:2,1:2]))