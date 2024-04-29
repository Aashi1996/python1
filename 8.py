import numpy as np
np4=np.array([1,2,3,4,5,6,7,8,9])
print(np4[4:])
print(np4[:4])
print(np4[-3:-1])
print(np4[1:5:2])
print(np4[::2])
print(np4.dtype)
np5=np.array(['apple','banana','orange'])
print(np5.dtype)
np6=np4.copy()
print(np6[0])

np7=np4.view()
np6[0]=99
np7[0]=99
print(np6)
print(np7)

np8=np.array([[2,4,6,8],[1,3,5,7]])
for j in np8:
    for i in j:
        print(i)
print()
for i in np8[0]:
    print(i)
for i in np8[1]:
    print(i)
