import numpy as np
import matplotlib.pyplot as plt

pmf_q = [0.05]*20
pmf_p = 5*[0.06]+[0.15,0.13,0.14,0.15,0.13]+[0]*10
simu_times = 1000
c=3
ran_sequence = []

for simu in range(simu_times):
    u = np.random.rand()
    q = np.random.randint(1,21)
    ratio = pmf_p[q-1]/pmf_q[q-1]/c
    if (u<ratio):
        ran_sequence.append(q)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.hist(ran_sequence,rwidth=0.9,alpha=0.8,bins=range(1,12))
ax.set_title('Histogram of random variable',fontsize=15)
ax.set_xlabel('Random variable value',fontsize=12)
ax.set_ylabel('Count',fontsize=12)

ax1 = ax.twinx()
ax1.step(range(1,12),[0.06]+pmf_p[0:10],'r')
ax1.set_ylabel('pmf',fontsize=12)
ax1.set_ylim([0,0.16])

plt.show()

ran_sequence = np.array(ran_sequence)
sample_mean = np.sum(ran_sequence)/ran_sequence.size
sample_variance = np.sum(np.square(ran_sequence-sample_mean))/(ran_sequence.size-1)
print(sample_mean,sample_variance)

expectation = 0
moment = 0
for i in range(10):
    expectation += pmf_p[i]*(i+1)
    moment += pmf_p[i]*(i+1)**2
varaince = moment-expectation**2
print(expectation,varaince)

sample_efficiency = len(ran_sequence)/simu_times
print(sample_efficiency)