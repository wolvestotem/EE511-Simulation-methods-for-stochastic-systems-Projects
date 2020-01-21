import random

#initial conditions
fair_coin_boundry = 0.5
experiment_number = 0
head_number = 0

#Input validation test
try:
    #input number of heads
    goal = int(input("Please input the positive number of heads:"))\
    #Simulation
    while(head_number<goal):
        if(random.random()>fair_coin_boundry):#Head
            head_number+=1
        experiment_number+=1

    #Output
    print(experiment_number)
    print(head_number)
except:
    print("Invalid input, please check")
