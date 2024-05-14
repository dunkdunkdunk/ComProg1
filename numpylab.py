import numpy as np
# l1=[1,2]
# l2=[4,5]
# a1=np.array(l1)
# a2=np.array(l2)

# dot product
# print(np.dot(a1,a2))
# print(a1@a2)

# k=np.array([l1,l2])
# print(k.shape)
# print(np.linalg.det(k))
# c=np.diag(k)
# print(c)
# print(np.diag(c))

a=np.arange(1,7)
b=np.arange(1,7)
print(np.concatenate((a,b.T)))