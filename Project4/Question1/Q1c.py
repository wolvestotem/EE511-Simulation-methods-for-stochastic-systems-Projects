import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

simu_times = 100000
x = np.random.rand(simu_times)
y = np.random.rand(simu_times)
f = np.exp(-np.square(x+y))
integral = sum(f)/f.size
print(integral)
