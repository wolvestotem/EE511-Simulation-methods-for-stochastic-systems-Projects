import numpy as np
import matplotlib.pyplot as plt

sample_size = 1000
sample_num = 1000
sample_mean = []
sample_variance = []
sample_standard_deviaion = []

for samples in range(sample_num):
    sample = np.random.rand(sample_size)*5-3
    mean = np.sum(sample)/sample_size
    sample_mean.append(mean)
    variance = np.sum(np.square(sample-mean))/(sample_size-1)
    sample_variance.append(variance)
    sample_standard_deviaion.append(np.sqrt(variance))

sample_mean.sort()
sample_variance.sort()
sample_standard_deviaion.sort()

# 95% confidence interval bootstrap
print(sample_mean[25],sample_mean[974])
print(sample_variance[25],sample_variance[974])
print(sample_standard_deviaion[25],sample_standard_deviaion[974])