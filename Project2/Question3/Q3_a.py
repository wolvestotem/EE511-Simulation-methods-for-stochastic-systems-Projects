import numpy as np
import matplotlib.pyplot as plt

M = 10
sample_size = 1000
sample = np.random.randint(M,size=sample_size)

plt.hist(sample,bins=10,rwidth=0.9,alpha=0.8,edgecolor='black')
plt.xlabel('Outcome Value',fontsize=12)
plt.ylabel('Count',fontsize=12)
plt.title('Histogram of uniform int random variable',fontsize=15)
plt.grid(axis='y',alpha=0.5)
plt.show()