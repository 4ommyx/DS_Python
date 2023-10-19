import numpy as np 

# Create ZeroMatrix 
a = np.zeros(5)
print("Zero Matrix : {} | Dimension : {} ".format(a, a.ndim))
print("-------------------------")
a = np.zeros(5, dtype=int)
print("Zero Matrix : {} | Dimension : {} ".format(a, a.ndim))
print("-------------------------")

# การสร้างMatrix ตั้งแต่2มิติขึ้นไป จะต้องใส่listและตามด้วย Row,Column 
# Ex : MatrixSize = [row, column]
a = np.zeros([2,2])
print("Zero Matrix : {} | Dimension : {} ".format(a, a.ndim))
print("-------------------------")
a = np.zeros([3,4], dtype=int)
print("Zero Matrix : {} | Dimension : {} ".format(a, a.ndim))
print("-------------------------")

# Create OneMatrix (รูปแบบการใช้งานคล้าย ZeroMatrix)
b = np.ones(10, dtype=int)
print("One Matrix : {} | Dimension : {} ".format(b, b.ndim))
print("-------------------------")
b = np.ones([3, 3], dtype=int)
print("One Matrix : {} | Dimension : {} ".format(b, b.ndim))
print("-------------------------")

# Create FullMatrix (คือการใส่ค่าใน Matrix ตัวนั้นๆให้เต็ม Matrix)
#  .full(a, b) --> a = ขนาดของ Matrix, b = สมาชิกที่ใส่ใน Matrix 
c = np.full(5, 10, dtype=int)
print("Full Matrix : {} | Dimension : {} ".format(c, c.ndim))
print("-------------------------")
c = np.full([3, 3], 7,  dtype=int)
print("FullMatrix : {} | Dimension : {} ".format(c, c.ndim))
print("-------------------------")