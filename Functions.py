import numpy as np
import matplotlib.pyplot as plt
    
#Initial State settings
def initialstate(initial_state):    
    while True:        
        
        if initial_state == 'A':
           IS = np.array([1, 0, 0, 0, 0, 0, 0, 0]) 
           break
            
        elif initial_state == 'B':
           IS = np.array([0, 1, 0, 0, 0, 0, 0, 0])
           break
            
        elif initial_state == 'C':
           IS = np.array([0, 0, 1, 0, 0, 0, 0, 0])
           break
           
        elif initial_state == 'D':
           IS = np.array([0, 0, 0, 1, 0, 0, 0, 0])
           break
           
        elif initial_state == 'E':
           IS = np.array([0, 0, 0, 0, 1, 0, 0, 0])
           break
           
        elif initial_state == 'F':
           IS = np.array([0, 0, 0, 0, 0, 1, 0, 0])
           break
           
        elif initial_state == 'G':
           IS = np.array([0, 0, 0, 0, 0, 0, 1, 0])
           break
           
        else:
            IS = np.array([0, 0, 0, 0, 0, 0, 0, 1])
            break
        
    #print(IS)
    #print(initial_state)   
    return(IS) 


#Calculation of stationary distribution
def stat_distr(T, I, IS, number_steps):    
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
    





















