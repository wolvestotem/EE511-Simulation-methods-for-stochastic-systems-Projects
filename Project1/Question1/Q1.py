import numpy as np
import matplotlib.pyplot as plt
import random

#Initial conditions
fair_coin_boundary = 0.5
count_number_Head = 0
experiment_times = 50
repeat_times = 1000
run_Head = 0
longest_run_Head = 0
count_number_Head_list = []

#Simulation
for r in range(repeat_times):
    run_Head = 0
    count_number_Head = 0
    for experiment in range(experiment_times):
        if(random.random()>fair_coin_boundary):#Head
            count_number_Head+=1
            run_Head+=1
            if(longest_run_Head < run_Head):
                longest_run_Head = run_Head
        else:#Tail
            run_Head = 0
    count_number_Head_list.append(count_number_Head)

#Output
print(longest_run_Head)
# print(count_number_Head_list)

#Graph
n,bins,patches = plt.hist(count_number_Head_list,bins=15,rwidth=0.9,edgecolor='black',alpha=0.8)
plt.xlim(min(count_number_Head_list),max(count_number_Head_list))
plt.grid(axis='y',alpha=0.8)
plt.ylabel('Times',fontsize=12)
plt.xlabel('Number of heads',fontsize=12)
plt.title('Number of Heads Histogram',fontsize=15)
plt.show()
