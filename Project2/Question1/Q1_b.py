import numpy as np
import matplotlib.pyplot as plt

sample_size = 1000
sample_num = 1
sample_mean = []
sample_variance = []

#Qustion 2 calculate the sample mean and variance
for samples in range(sample_num):
    sample = np.random.rand(sample_size)*5-3
    mean = np.sum(sample)/sample_size
    sample_mean.append(mean)
    variance = np.sum(np.square(sample-mean))/(sample_size-1)
    sample_variance.append(variance)

print(sample_mean)
print(sample_variance)