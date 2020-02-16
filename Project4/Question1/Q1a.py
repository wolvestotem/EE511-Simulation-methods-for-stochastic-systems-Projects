import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

simu_times = 1000
ran = np.random.normal(2,1,simu_times)
pos_ran = ran[ran>=0]
pos_ran = pos_ran[pos_ran<=2]

neg_ran = np.random.normal(-2,1,simu_times)
neg_ran = neg_ran[neg_ran<=0]
neg_ran = neg_ran[neg_ran>=-2]

pos_y = np.sqrt(2*np.pi)*np.exp(1.5*np.square(pos_ran)-pos_ran+2)*0.477
neg_y = np.sqrt(2*np.pi)*np.exp(1.5*np.square(neg_ran)+3*neg_ran+2)*0.477

ran = 4*np.random.rand(int(simu_times*0.477))-2
y = 4*np.exp(ran+np.square(ran))

integral_pos = np.sum(pos_y)/pos_y.size
integral_neg = np.sum(neg_y)/neg_y.size
print(sum(y)/y.size)
print(integral_neg+integral_pos)