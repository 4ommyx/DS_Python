import numpy as np

# Empty Matrix (คือการ Random ค่าใส่เข้าไปใน Matrix) 
# ซึ่งในส่วนใหญ่นั้นจะนำเอา ขนาดของ Matrix ไปใช้เป็นประโยชน์มากกว่า
a = np.empty(5)
print("EmptyMatrix : {} | Dimension : {} ".format(a, a.ndim))
print("-------------------------")
a = np.empty([3, 3])
print("EmptyMatrix : {} | Dimension : {} ".format(a, a.ndim))
print("-------------------------")

# Identity Matrix (คือ Matrix ที่มีค่าบน Diagonal เป็น 1 (แนวทะแยง) )
b = np.identity(4, dtype = int)
print("IdentityMatrix : {} | Dimension : {} ".format(b, b.ndim))
print("-------------------------")
b = np.identity(5, dtype = int)
print("IdentityMatrix : {} | Dimension : {} ".format(b, b.ndim))
print("-------------------------")

# Eye Function (คือการแสดงค่า Identity Matrix แบบไม่จัตุรัส) 
# รวมถึงการ Shift diagonol ด้วยค่า K ->> 
# K : Positive shift right , K : Negative shift left
c = np.eye(3, 2)
print("IdentityMatrix(eve) : {} | Dimension : {} ".format(c, c.ndim))
print("-------------------------")
c = np.eye(5,4)
print("IdentityMatrix(eve) : {} | Dimension : {} ".format(c, c.ndim))
print("-------------------------")
c = np.eye(5,4,k=1)
print("IdentityMatrix(eve) K = 1 : {} | Dimension : {} ".format(c, c.ndim))
print("-------------------------")
c = np.eye(5,4,k=-2)
print("IdentityMatrix(eve) K = -2 : {} | Dimension : {} ".format(c, c.ndim))
print("-------------------------")

