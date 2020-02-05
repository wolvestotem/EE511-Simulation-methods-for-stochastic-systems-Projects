import numpy as np
import matplotlib.pyplot as plt

sample_size = 1000
X_k = np.random.rand(sample_size)
X_k1 = X_k[1:-2]
X_k2 = X_k[2:-1]
X_k3 = X_k[3:]
X_k = X_k[:-3]
Y = X_k-2*X_k1+0.5*X_k2-X_k3
sample_size = sample_size-3

X_k_mean = sum(X_k)/sample_size
Y_mean = sum(Y)/sample_size
cov = sum((X_k-X_k_mean)*(Y-Y_mean))/sample_size
print(cov)