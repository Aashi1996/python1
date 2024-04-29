import numpy as np
np1=np.array([1,2,3,4,5])
print(np1)
print(type(np1))
print(np1.ndim)

np2=np.array([[2,4,6,8],[1,3,5,7]])
print(np2)
print(np2.ndim)
print(np2[0])
print(np2[1])
print(np2[0][0])
np3=np2[0]
print(np3[0:2])
print(np3)
print(np2[0][0:2])
print(np2[-1])
np4=np.array([1,2,3,4,5,6,7,8,9])
print(np4[4:])
