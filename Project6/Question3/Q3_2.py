import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import levy_stable

# alpha = 0.5
alpha = 0.5
Kalpha = alpha
beta = 0.75
beta2 = np.arctan(beta*np.tan(np.pi*alpha/2))*2/np.pi/Kalpha
gamma0 = -0.5*np.pi*beta2*Kalpha/alpha
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

# alpha = 1 beta = 0
alpha = 1
beta = 0.75
beta2 = beta
result = []

for i in range(N):
    W = np.random.exponential(1)
    gamma = np.random.uniform(-np.pi/2,np.pi/2)
    X = (np.pi/2+beta2*gamma)*np.tan(gamma)-beta2*np.log(W*np.cos(gamma)/(np.pi/2+beta2*gamma))
    result.append(X)
result = np.array(result)

plt.hist(result,alpha=0.7,edgecolor="black",bins=20,range=(-10,10),normed=True)
plt.plot(x,levy_stable.pdf(x,alpha,beta),color="red")
plt.ylabel("Frequency", fontsize=12)
plt.title("Histogram of alpha=1 standard stable r.v.")
plt.show()

# alpha = 1.8
alpha = 1.8
Kalpha = alpha-2
beta = 0.75
beta2 = np.arctan(beta*np.tan(np.pi*alpha/2))*2/np.pi/Kalpha
gamma0 = -0.5*np.pi*beta2*Kalpha/alpha
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
beta = 0.75
Kalpha = alpha-2
gamma0 = 0
result = []

for i in range(N):
    W = np.random.exponential(1)
    gamma = np.random.uniform(-np.pi/2,np.pi/2)
    X = np.sin(alpha*(gamma-gamma0))/np.cos(gamma)**(1/alpha)*(np.cos(gamma-alpha*(gamma-gamma0))/W)**((1-alpha)/alpha)
    result.append(X)
result = np.array(result)

plt.hist(result,alpha=0.7,edgecolor="black",bins=20,range=(-10,10),density=True)
plt.plot(x,levy_stable.pdf(x,alpha,beta),color="red")
plt.ylabel("Frequency", fontsize=12)
plt.title("Histogram of alpha=2 standard stable r.v.")
plt.show()
