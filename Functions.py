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
























