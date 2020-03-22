import numpy as np
import matplotlib.pyplot as plt
import time


start_box = time.time()
N = 1000000 #no of samples
M1 = 1 # Mean of X
M2 = 2 # Mean of Y
V1 = 4 # Variance of X
V2 = 9 # Variance of Y

u1 = np.random.rand(N,1)
u2 = np.random.rand(N,1)

#  Generate X and Y that are N(0,1) random variables and independent
X = np.sqrt(-2*np.log(u1))*np.cos(2*np.pi*u2)
Y = np.sqrt(-2*np.log(u1))*np.sin(2*np.pi*u2)

# Scale them to a particular mean and variance 
x = np.sqrt(V1)*X + M1 # x~ N(M1,V1)
y = np.sqrt(V2)*Y + M2 # y~ N(M2,V2)

end_box = time.time()
print('time',end_box - start_box)

covariance_xy = np.dot((x-M1).T, y-M2)/N
print("covariance",covariance_xy)

A = x+y
t = np.arange(-5,11,0.01)
ft = np.e**(-np.square(t-3)/26)/np.sqrt(26*np.pi)
plt.hist(A, alpha = 0.7, edgecolor = "black", normed=True)
plt.plot(t,ft,color="red")
plt.ylabel("frequency",fontsize=12)
plt.title("Histogram of A",fontsize=15)
plt.show()

A_meanBM = np.sum(A)/N
A_varianceBM = np.sum(np.square(A-A_meanBM))/(N-1)
print(A_meanBM, A_varianceBM)

start_mar = time.time()
X = []
Y = []
i = 0
while i<1000000:
    u1 = 2*np.random.rand()-1
    u2 = 2*np.random.rand()-1
    s = u1*u1 + u2*u2
    if s < 1:
        X.append(np.sqrt(-2*np.log(s)/s)*u1)
        Y.append(np.sqrt(-2*np.log(s)/s)*u2)
        i = i+1
X = np.array(X)
Y = np.array(Y)
size = X.size       
# Scale them to a particular mean and variance 
x = np.sqrt(V1)*X + M1 # x~ N(M1,V1)
y = np.sqrt(V2)*Y + M2 # y~ N(M2,V2)

end_mar = time.time()
print('time',end_mar - start_mar)

A = x+y
A_meanPM = np.sum(A)/size
A_variancePM = np.sum(np.square(A-A_meanPM))/(size-1)
covariance = np.dot((x-M1).T,y-M2)/size
print(A_meanBM, A_variancePM)
print(covariance)
