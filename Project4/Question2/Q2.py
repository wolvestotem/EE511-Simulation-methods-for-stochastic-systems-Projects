import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

n = 1000
z1 = np.random.randn(n)
z2 = np.random.randn(n)
z3 = np.random.randn(n)
z4 = np.random.randn(n)
x = np.square(z1)+np.square(z2)+np.square(z3)+np.square(z4)

x=sorted(x)
t = np.arange(min(x),max(x),0.01)
chi_square = stats.chi2.cdf(t,4)
plt.step(x,np.arange(1/n,1+1/n,1/n),label='empirical',color='blue',where='post')
plt.plot(t,chi_square,label='theoretical',color='red')
plt.title('Empirical and theoretical CDF',fontsize=15)
plt.legend()
# plt.show()

maxdiff = max(abs(stats.chi2.cdf(x,4)-np.arange(1/n,1+1/n,1/n)))
print(maxdiff)

percentiles = 0.9
for i in range(n):
    if ((i+1)/n >= percentiles):
        p_edf = x[i]
        break
print('p_edf=',p_edf,i)

p_thrm = stats.chi2.ppf(percentiles,4)
print('p_thrm=',p_thrm) 