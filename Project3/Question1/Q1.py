import numpy as np
import matplotlib.pyplot as plt
import random

simu_times = 1000
lot_num = 125
defective_unit_num = 6
test_num = 5
reject_times = 0

for simulation in range(simu_times):
    result = 0
    lot = np.append(np.zeros((lot_num-defective_unit_num)),np.ones((defective_unit_num)))
    sample = random.sample(range(125),5)
    for  i in sample:
        result = result or lot[i]
    if result:
        reject_times += 1
    
print(reject_times)
