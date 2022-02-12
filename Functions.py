import numpy as np
import matplotlib.pyplot as plt
import random

    
#Initial State settings
def initialstate(initial_state):
    init_state_dict = {'A': np.array([1, 0, 0, 0, 0, 0, 0, 0]),
                       'B': np.array([0, 1, 0, 0, 0, 0, 0, 0]),
                       'C': np.array([0, 0, 1, 0, 0, 0, 0, 0]),
                       'D': np.array([0, 0, 0, 1, 0, 0, 0, 0]),
                       'E': np.array([0, 0, 0, 0, 1, 0, 0, 0]),
                       'F': np.array([0, 0, 0, 0, 0, 1, 0, 0]),
                       'G': np.array([0, 0, 0, 0, 0, 0, 1, 0]),
                       'H': np.array([0, 0, 0, 0, 0, 0, 0, 1]) }    
    if initial_state not in init_state_dict.keys():
        raise ValueError("Invalid initial state. It must be chosen among: {A, B, C, D, E, F, G, H}")                             
    IS = init_state_dict[initial_state]          
    return(IS) 


#Calculation of stationary distribution
def stat_distr(T, I, IS, number_steps):    
    #the number of steps must be at least 10 in order to reach stationarity
    if number_steps < 10:
        raise ValueError("Invalid number of steps. It must be at least equal to 10 in order to reach stationarity")   
    number_steps = number_steps - 2   
    A = np.array([I*T]) #first matrix multiplication result
    i = 0 #index
    while i < number_steps:       
        A[i] = A[i-1]*T
        A = np.append(A, [A[i]], axis=0)   
        i += 1       
    C = np.array([I*T])
    A = np.concatenate((C,A),axis= 0) 
    A = A.reshape(len(A),8)
    IS = IS.reshape(1,8)
    A = np.concatenate((IS,A),axis= 0)       
    return(A)
 

#Plot function
def plot_func(A, B):
    a = np.arange(len(A)) #array which represents the number of steps
    plt.plot(a, B[0], 'yellow', label='State A')
    plt.plot(a, B[1], 'pink', label='State B')
    plt.plot(a, B[2], 'aquamarine', label='State C')
    plt.plot(a, B[3], 'darkturquoise', label='State D')
    plt.plot(a, B[4], 'orange', label='State E')
    plt.plot(a, B[5], 'mediumblue', label='State F') 
    plt.plot(a, B[6], 'forestgreen', label='State G')
    plt.plot(a, B[7], 'purple', label='State H')
    plt.legend()
    plt.xlabel('Number of steps')
    plt.ylabel('Probability')   
    plt.show() 
    return()

    
#Random walk generation function 
def rnd_walk(number_steps, T, initial_state, states, seed):
    T = np.array(T)
    path = [] #list which will contain the path
    path.append(initial_state) #initial state added to the list in position 0
    #Raise error if random seed is not a number
    if isinstance(seed, str):
        raise ValueError("Invalid seed. It must be a number")        
    #path simulation     
    weights_dict = {'A': T[0], 'B': T[1], 'C': T[2], 'D': T[3], 'E': T[4], 'F': T[5], 'G': T[6], 'H': T[7] }                                                                                                  
    random.seed(seed)   
    for i in range(number_steps):               
        next_state = random.choices(states, weights_dict[path[i]])
        path.append(next_state[0])            
    return(path) 




















