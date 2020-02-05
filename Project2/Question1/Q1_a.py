import numpy as np
import matplotlib.pyplot as plt

sample_size = 1000
sample_num = 1
sample = np.random.rand(sample_size)*5-3
# print(sample)

plt.hist(sample,rwidth=0.9,bins=10,edgecolor='black',alpha=0.8,range=(-3,2))
plt.xlim(min(sample),max(sample))
# plt.grid()
plt.xlabel('random variable value',fontsize=12)
plt.ylabel('count',fontsize=12)
plt.title('Histogram for outcomes',fontsize=15)
plt.show()
