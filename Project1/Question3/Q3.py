import numpy as np
import matplotlib.pyplot as plt
import random

#Initial conditions
fair_coin_boundary = 0.5
experiment_times = 100
repeat_times = 1
run_Head = 0
run_length_list = []

#Simulation
for r in range(repeat_times):
    run_Head = 0
    for experiment in range(experiment_times):
        if(random.random()>fair_coin_boundary):#Head
            run_Head+=1
        else:#Tail
            if(run_Head!=0):
                run_length_list.append(run_Head)
            run_Head = 0

#Output
print(run_length_list)

#Graph
n,bins,patches = plt.hist(run_length_list,bins=6,rwidth=0.9,edgecolor='black',alpha=0.8)
plt.xlim(min(run_length_list),max(run_length_list))
plt.grid(axis='y',alpha=0.8)
plt.ylabel('Counts',fontsize=12)
plt.xlabel('Heads run length',fontsize=12)
plt.title('Heads run length Histogram',fontsize=15)
plt.show()
