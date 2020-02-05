import numpy as np
import matplotlib.pyplot as plt

sample_size = 1000
X_k = np.random.rand(sample_size)
X_k1 = X_k[1:]
X_k = X_k[:-1]
sample_size = sample_size-1

X_k_mean = sum(X_k)/sample_size
X_k1_mean = sum(X_k1)/sample_size
cov = sum((X_k-X_k_mean)*(X_k1-X_k1_mean))/sample_size
print(cov)