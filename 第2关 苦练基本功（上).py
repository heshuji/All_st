
import numpy as np
print(np.__version__)
# 在array函数中直接传入一个列表，即可创建一个数组
nparray = np.array([0,1,2,3,4,5,6,7,8,9]) 
print(nparray.shape)
print(nparray[3])
nparray[3]=200
print(nparray[3])
print(nparray.dtype)
# nparray[3]='shujinb'
# print(nparray[3])