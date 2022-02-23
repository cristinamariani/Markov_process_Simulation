import numpy as np
import matplotlib.pyplot as plt
import random

    
#Initial State settings
def initialstate(initial_state):
    """This function defines the initial distribution of the Markov process. 
    
    Parameters
    ----------
    initial_state (string): initial state (state 0) of the process
    
    Returns
    -------
    IS (numpy array): initial distribution related to the initial state  
    
    Raises
    ------
    ValueError if the chosen state is not in the list {A, B, C, D, E, F, G, H} 
    """    
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
    return IS 
 

#Calculation of stationary distribution
def prob_distr(Transition_matrix, InitialState_array, number_steps): 
    """This function calculates the probability distributions of the Markov process. 
    
    Parameters
    ----------
    Transition_matrix (numpy matrix): 8x8 transition matrix of the system
    InitialState_array (numpy array): initial distribution related to the initial state
    number_steps (int): number of steps performed during the process
    
    Returns
    -------
    A (numpy array): array which contains all the calculated probability distributions    
    """ 
    I = np.matrix([InitialState_array])
    number_steps = number_steps - 2   
    A = np.array([I*Transition_matrix]) #first matrix multiplication result
    i = 0 #index
    while i < number_steps:       
        A[i] = A[i-1]*Transition_matrix
        A = np.append(A, [A[i]], axis=0)   
        i += 1       
    C = np.array([I*Transition_matrix])
    A = np.concatenate((C,A),axis= 0) 
    A = A.reshape(len(A),8)
    InitialState_array = InitialState_array.reshape(1,8)
    A = np.concatenate((InitialState_array,A),axis= 0)       
    return A 
  

#Plot function
def plot_func(A, B): # A = array which contains the probability distributions as elements, B = transpose of A
    """This function plots the probabilities to reach each state versus the number of steps.
    
    Parameters
    ----------
    A (numpy array): array which contains all the calculated probability distributions
    B (numpy array): transpose of A, represents the probabilities to reach each state
    """ 
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

    
#Random walk generation function 
def rnd_walk(number_steps, Transition_matrix, initial_state, states, seed):
    """This function generates a possible random walk "traveled" by the system during the process.
    
    Parameters
    ----------
    number_steps (int): number of steps performed during the process
    Transition_matrix (numpy matrix): 8x8 transition matrix of the system
    initial_state (string): initial state (state 0) of the process
    states (list): list of the possible states
    seed (int): random seed
    
    Returns
    -------
    path (list): random walk "traveled" by the system    
    """
    Transition_matrix = np.array(Transition_matrix)
    path = [] #list which will contain the path
    path.append(initial_state) #initial state added to the list in position 0      
    #path simulation     
    weights_dict = {'A': Transition_matrix[0], 
                    'B': Transition_matrix[1], 
                    'C': Transition_matrix[2], 
                    'D': Transition_matrix[3], 
                    'E': Transition_matrix[4], 
                    'F': Transition_matrix[5], 
                    'G': Transition_matrix[6], 
                    'H': Transition_matrix[7]}                                                                                                  
    random.seed(seed)   
    for i in range(number_steps):               
        next_state = random.choices(states, weights_dict[path[i]])
        path.append(next_state[0])            
    return path 


#Random walk check function
def check_rnd_walk(path):
    """This function checks that the random walk does not contain transitions with transition probability equal to 0.
    
    Parameters
    ----------
    path (list): random walk "traveled" by the system
    
    Returns
    -------
    bool: True if the random walk does not travel forbidden transitions, False otherwise   
    """
    forbidden_transitions = [['B', 'D'], ['C', 'H'], ['E', 'A'], ['E', 'B'], ['F', 'E'], ['H', 'G']] #couples of states which have transition probability = 0
    i = 1
    while i < len(path):
        if [path[i-1], path[i]] in forbidden_transitions:
            return False
            raise ValueError("Forbidden transition made!")
        i += 1
    return True
            

















