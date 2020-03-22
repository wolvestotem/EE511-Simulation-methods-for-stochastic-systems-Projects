import numpy as np
import matplotlib.pyplot as plt

N = 100000
theta = 5.5
theta_g = 6
c = 6/5.5
result = []

for i in range(N):
    u = np.random.rand()
    x = np.random.exponential(theta_g)
    f = 1/theta*np.exp(-x/theta)
    g = 1/theta_g*np.exp(-x/theta_g)
    if (f/(c*g))>=u:
        result.append(x)

result = np.array(result)
t = np.arange(0,30,0.01)
pdf = 1/theta*np.exp(-t/theta)
print(result.size)

plt.hist(result,alpha = 0.7, edgecolor = "black",bins = 20, normed=True, range=(0,30))
plt.plot(t,pdf,color="red")
plt.title("Histogram of the exp(5.5) random variable", fontsize=15)
plt.ylabel("Frequency", fontsize=12)
plt.show()

accept_rate = result.size/N
print(accept_rate, 1/c)
