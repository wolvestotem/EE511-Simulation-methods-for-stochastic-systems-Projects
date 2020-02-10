import numpy as np
import matplotlib.pyplot as plt

simu_num = 10000
boundary = 4
N = []

for i in range(simu_num):
    sample = []
    while(np.sum(sample)<=boundary):
        sample.append(np.random.rand(1))

    N.append(len(sample)) 
# print(N)

num = np.unique(N)
plt.hist(N,rwidth=0.9,alpha=0.8,edgecolor='black',bins=range(min(num),max(num)+1))
plt.xlabel('Value of N',fontsize=12)
plt.ylabel('Count',fontsize=12)
plt.title('Histogram of N(Size=10000)')
plt.show()

Expectation = sum(N)/len(N)
print(Expectation)


