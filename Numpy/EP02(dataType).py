import numpy as np 
lis = [1, 2, 3, 4, 5]
# สามารถเปลี่ยน datatype ทั้ง array ให้เป็นรูปแบบอื่นได้
dt0 = np.array(lis,dtype=int)
print("Int Type : {}".format(dt0))
print("-------------------------")
dt0 = np.array(lis,dtype="str")
print("String Type : {}".format(dt0))
print("-------------------------")
dt0 = np.array(lis,dtype="complex")
print("Complex Type : {}".format(dt0))
print("-------------------------")
dt0 = np.array(lis,dtype="float")
print("Float Type : {}".format(dt0))
print("-------------------------")
print("Result {}".format(dt0[0]+dt0[1]))