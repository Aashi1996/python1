import numpy as np
np1=np.array([2,4,6,8])
np2=np.array([1,3,5,7])
np3=np.concatenate((np1,np2))
print(np3)

np3=np.array([[1,2],[3,4]])
np4=np.array([[5,6],[7,8]])
np5=np.concatenate((np3,np4),axis=0)
print(np5)
print()
np6=np.concatenate((np3,np4),axis=1)
print(np6)

np7=np.stack((np3,np4),axis=1)
print(np7)

np8=np.hstack((np3,np4))
print(np8)

np9=np.vstack((np3,np4))
print(np9)
print()
np10=np.dstack((np3,np4))
print(np10)
