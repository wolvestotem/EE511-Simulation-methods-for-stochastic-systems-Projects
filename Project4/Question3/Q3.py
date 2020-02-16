import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('faithful.dat.txt',skiprows=26)
roi = data[0:15,2]
mean = sum(data[:,2])/data.shape[0]

xbar = sum(roi)/roi.size
sn = np.sqrt(1/(roi.size-1)*np.sum(np.square(xbar-roi)))
t_alpha = 2.145
CI_statistical = (xbar-t_alpha*sn/np.sqrt(15),xbar+t_alpha*sn/np.sqrt(15))
print(sn,xbar,CI_statistical,mean)

samples = 1000
xbarlist = []
for i in range(samples):
    sample = []
    for j in range(roi.size):
        u = np.random.randint(0,roi.size)
        sample.append(roi[u])
    xbarlist.append(sum(sample)/len(sample))
xbarlist = sorted(xbarlist,reverse=False)
CI_bootstrap = (xbarlist[25],xbarlist[974])
print(CI_bootstrap)

whole = data[:,2]
xbar = sum(whole)/whole.size
sn = np.sqrt(1/(whole.size-1)*np.sum(np.square(xbar-whole)))
z_alpha = 1.96
CI_statistical = (xbar-z_alpha*sn/np.sqrt(whole.size),xbar+z_alpha*sn/np.sqrt(whole.size))
print(sn,xbar,CI_statistical,mean)

samples = 1000
xbarlist = []
for i in range(samples):
    sample = []
    for j in range(whole.size):
        u = np.random.randint(0,whole.size)
        sample.append(whole[u])
    xbarlist.append(sum(sample)/len(sample))
xbarlist = sorted(xbarlist)
CI_bootstrap = (xbarlist[25],xbarlist[974])
print(CI_bootstrap)


