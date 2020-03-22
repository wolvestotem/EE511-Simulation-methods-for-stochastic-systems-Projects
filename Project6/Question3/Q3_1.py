import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import levy_stable

# alpha = 0.5
alpha = 0.5
Kalpha = alpha
beta = 0
gamma0 = 0
N = 1000
result = []

for i in range(N):
    W = np.random.exponential(1)
    gamma = np.random.uniform(-np.pi/2,np.pi/2)
    X = np.sin(alpha*(gamma-gamma0))/np.cos(gamma)**(1/alpha)*(np.cos(gamma-alpha*(gamma-gamma0))/W)**((1-alpha)/alpha)
    result.append(X)
result = np.array(result)

# x = np.arange(levy_stable.ppf(0.01,alpha,beta),levy_stable.ppf(0.99,alpha,beta),0.01)
x = np.arange(-10,10,0.1)

plt.hist(result,alpha=0.7,edgecolor="black",bins=20,range=(-10,10),normed=True)
plt.plot(x,levy_stable.pdf(x,alpha,beta),color="red")
plt.ylabel("Frequency", fontsize=12)
plt.title("Histogram of alpha=0.5 standard stable r.v.")
plt.show()

# alpha = 1 beta = 0------standard Cauchy distribution
alpha = 1
beta = 0
rv = np.random.standard_cauchy(N)

plt.hist(rv,alpha=0.7,edgecolor="black",density=True,bins=20,range=(-10,10))
plt.plot(x, 1/(np.pi*(1+np.square(x))),color="red")
plt.title("Histogram of alpha=1 standard stable r.v.")
plt.ylabel("Frequency", fontsize=12)
plt.show()

# alpha = 1.8
alpha = 1.8
beta = 0
gamma0 = 0
result = []

for i in range(N):
    W = np.random.exponential(1)
    gamma = np.random.uniform(-np.pi/2,np.pi/2)
    X = np.sin(alpha*(gamma-gamma0))/np.cos(gamma)**(1/alpha)*(np.cos(gamma-alpha*(gamma-gamma0))/W)**((1-alpha)/alpha)
    result.append(X)
result = np.array(result)

plt.hist(result,alpha=0.7,edgecolor="black",bins=20,range=(-10,10),normed=True)
plt.plot(x,levy_stable.pdf(x,alpha,beta),color="red")
plt.ylabel("Frequency", fontsize=12)
plt.title("Histogram of alpha=1.8 standard stable r.v.")
plt.show()

# alpha = 2; beta = 0----------standard Gaussian distribution
alpha = 2
beta = 0
rv = np.random.randn(N)

plt.hist(rv,alpha=0.7,edgecolor="black",bins=20,range=(-10,10),normed=True)
plt.plot(x,1/np.sqrt(2*np.pi)*np.exp(-0.5*np.square(x)),color="red")
plt.ylabel("Frequency", fontsize=12)
plt.title("Histogram of alpha=2 standard stable r.v.")
plt.show()
