import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

simu_times = 100000
pos_ran = np.random.rand(simu_times)
pos_y = np.exp(-np.square(1/pos_ran-1))*(1/np.square(pos_ran))
neg_ran = -np.random.rand(simu_times)
neg_y = np.exp(-np.square(1/neg_ran+1))*(1/np.square(neg_ran))
integral = sum(pos_y)/pos_y.size +sum(neg_y)/neg_y.size
print(integral)
