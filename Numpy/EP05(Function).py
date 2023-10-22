# Linspace คือการใส่ข้อมูล ใน Array 1 มิติ 
# โดยจะเริ่มที่จุด start ---> stop ซึ่งระยะห่างของแต่ละค่าจะมีค่าเท่ากัน 
# โดย defult จะใส่ค่าใน Array ทั้งหมด 50 ค่า
import numpy as np
a = np.linspace(1,10)
print("Linspace : {} Dimension {}".format(a, a.ndim))
print("---------------------")
a = np.linspace(0,10,5)
print("Linspace : {} Dimension {}".format(a, a.ndim))
print("---------------------")

# arange การใช้งานจะคล้ายๆกับ range ใน for 
# arange(start, stop, step) ซึ่งค่าที่ใส่ใน array จะเป็น array 1 มิติ
b = np.arange(1,10)
print("Arange : {} Dimension {}".format(b, b.ndim))
print("---------------------")
b = np.arange(1,12,2,  dtype = complex)
print("Arange : {} Dimension {}".format(b, b.ndim))
print("---------------------")

# random จะ สุ่มค่าใส่ array โดยที่ค่าของสมาชิกแต่ละตัวจะอยู่ในช่วง 0 ถึง 1
# random.random([row, column])
c = np.random.random(5)
print("Ramdom : {} Dimension {}".format(c, c.ndim))
print("---------------------")
c = np.random.random([5, 4])
print("Ramdom : {} Dimension {}".format(c, c.ndim))
print("---------------------")

