import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

N = 2000
X = []
for i in range(N):
    x = 0.4*np.random.normal(-1,1)+0.6*np.random.normal(1,1) #mu and std
    X.append(x)
X = np.array(X)
mu = 0.2
variance = 1
t = np.linspace(norm.ppf(0.05,mu),norm.ppf(0.95,mu),100)
plt.hist(X,alpha=0.7, edgecolor='black',density=True,bins=20)
plt.plot(t,norm.pdf(t,mu),'r')
plt.title("histogram and pdf of mixture",fontsize=15)
plt.show()