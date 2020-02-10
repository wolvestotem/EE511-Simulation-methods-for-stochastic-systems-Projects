import numpy as np
import matplotlib.pyplot as plt
import random
import math

ran_sequence_num = 1000
simu_num = 1000
j = 60
ran_sequence = []
N = []
p=10 #OR any constant number
weight = [p/i for i in range(1,61)]
total_weight = sum(weight)

#Generate random sequence Xk
for i in range(ran_sequence_num):
    u = random.uniform(0,total_weight)
    ran = 1
    while (sum(weight[0:ran])<=u):
        ran+=1
    ran_sequence.append(ran)

plt.figure(1)
plt.hist(ran_sequence,rwidth=0.9,alpha=0.8)
plt.title('Histogram of random sequence Xk',fontsize=15)
plt.xlabel('Random value',fontsize=12)
plt.ylabel('Count',fontsize=12)
# plt.show()

#Generate random variable Nj
for simu in range(simu_num):
    i = 0
    while(True):
        u = random.uniform(0,total_weight)
        ran = 1
        while (sum(weight[0:ran])<=u):
            ran+=1
        if (ran == j):
            N.append(i)
            break
        i+=1

plt.figure(2)
plt.hist(N,rwidth=0.9,alpha=0.8,bins=10)
plt.title('Histogram of random variable Nj',fontsize=15)
plt.xlabel('Random value',fontsize=12)
plt.ylabel('Count',fontsize=12)
plt.show()

#Calculate the sample expectation and variance
N = np.array(N)
expected_N = np.sum(N)/N.size
variance_N = np.sum(np.square(N-expected_N))/(N.size-1)
print(expected_N,variance_N)

#The random variable Nj is geometric
p60 = p/60/total_weight
threm_E = 1/p60
threm_V = (1-p60)/math.pow(p60,2)
print(threm_E,threm_V)