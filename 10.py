import numpy as np
np1=np.array([2,4,6,8,10,12,14,16,18,20])
np2=np.array([1,3,5,7])
np3=np.array_split(np1,2)
print(np3)

np3=np.array_split(np1,3)
print(np3)

np3=np.array_split(np1,4)
print(np3)

np4=np.where(np1==4)
print(np4)
