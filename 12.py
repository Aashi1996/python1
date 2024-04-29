import numpy as np
np1=np.array([2,4,6,8,10,12,14,16,18,20,4])

np2=np.where(np1==4)
print(np2)

np3=np.where(np1%4==0)
print(np3)

np4=np.searchsorted(np1,3)
print(np4)

np5=np.sort(np1)
print(np5)
