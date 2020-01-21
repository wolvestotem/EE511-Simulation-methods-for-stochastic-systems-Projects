import numpy as np
import matplotlib.pyplot as plt
import random

#Initial conditions
fair_coin_boundary = 0.2
experiment_times = 200
repeat_times = 1
run_Head = 0
longest_run_Head = 0
count_number_Head_list = []
count_number_Head = 0

#Simulation
for r in range(repeat_times):
    run_Head = 0
    for experiment in range(experiment_times):
        if(random.random()>fair_coin_boundary):#Head
            count_number_Head_list.append(1)
            count_number_Head+=1
            run_Head+=1
            if(longest_run_Head < run_Head):
                longest_run_Head = run_Head
        else:#Tail
            run_Head = 0
            count_number_Head_list.append(0)

#Output
print(longest_run_Head)
print(count_number_Head)

#Graph
n,bins,patches = plt.hist(count_number_Head_list,bins=2,rwidth=1,edgecolor='black',alpha=0.8,range=(-0.5,1.5))
# plt.xlim(min(count_number_Head_list),max(count_number_Head_list))
plt.grid(axis='y',alpha=0.8)
plt.ylabel('Counts',fontsize=12)
plt.xlabel('Heads=1; Tails=0',fontsize=12)
plt.title('Histogram for Bernoulli outcomes',fontsize=15)
plt.show()
