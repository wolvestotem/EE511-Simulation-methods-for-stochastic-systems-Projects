import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb,perm
import math

simu_times = 1000
lmbda = 120
n = 4000
p = lmbda/n
sample_B = []
sample_P = []
pmf_poisson = []
pmf_x = np.arange(85,156,1,dtype=float)

for trial in range(simu_times):
    u = np.random.rand(1,n)
    bernoulli = u<p
    sample_B.append(np.sum(bernoulli))

pmf_binomial = [comb(n,k)*pow(p,k)*pow(1-p,n-k) for k in pmf_x]
pmf_poisson = [pow(lmbda,k)*7.66*10**(-53)/perm(k,k) for k in pmf_x]
# print(pmf_poisson)

fig,ax = plt.subplots(1,2)
ax[0].hist(sample_B,rwidth=0.9,edgecolor='black',alpha=0.8)
# ax[0].step(pmf_x,pmf_binomial,'r')
ax[0].set_title('Histogram of Poisson likely Binomial',fontsize=15)
ax[0].set_ylabel('Count',fontsize=12)

ax0 = ax[0].twinx()
ax0.step(pmf_x,pmf_binomial,'r')
ax0.set_ylabel('Probability',fontsize=12)

sample_P = np.random.poisson(lmbda,simu_times)

ax[1].hist(sample_P,rwidth=0.9,edgecolor='black',alpha=0.8)
# ax[1].step(pmf_x,pmf_poisson,'r')
ax[1].set_title('Histogram of Poisson variable',fontsize=15)
ax[1].set_ylabel('Count',fontsize=12)

ax1 = ax[1].twinx()
ax1.step(pmf_x,pmf_poisson,'r')
ax1.set_ylabel('Probablity',fontsize=12)

plt.show()
