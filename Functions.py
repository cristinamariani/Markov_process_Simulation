import numpy as np

    
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





















