import numpy as np
import matplotlib.pyplot as plt
import random

a=np.array([[1,2,3],[4,5,6]])
b=np.arange(12)
b=b.reshape(6,2)
c=np.ones((5,1),dtype=np.int)
d=np.arange(1,10,3)#arange函数----步长
e=np.linspace(1,10,10,dtype=np.int)#linspace函数---步数
#print(e)

if(False):
    print("hello")
else:
    # print("world")
    a=1

Array = np.zeros((2,5),dtype=np.int)
Array[0,2]=3
# print(Array)

# j=0
# for i in range(2):
#     print('j=',j)
#     for j in range(3):
#         print(j)

a = np.arange(0,10,2)
print(a[:-1])#舍去最后一位
print(a)