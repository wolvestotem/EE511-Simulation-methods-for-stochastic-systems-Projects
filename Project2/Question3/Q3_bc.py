import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as scis

M = 10
sample_size = 1000

#Question number 3(b) Code
# sample = np.random.randint(10,size=sample_size)
#Question number 3(b) Code
sample = np.random.randint(1,11,size=sample_size)

observed = []
for i in range(10):
    observed.append(sample[sample == i].size)
expected = 100*np.ones((10),dtype=np.int)

(kvalue,pvalue)=scis.chisquare(observed,expected)
print(kvalue,pvalue)

