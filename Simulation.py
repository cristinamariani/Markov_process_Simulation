import numpy as np 
import functions
import configparser


config = configparser.ConfigParser()
config.read('configuration.txt')


print("\n")
print("****************************************************")
print("Eight-state Discrete-time Markov process Simulation")
print("****************************************************")


#Transition Matrix

print("\nTransition matrix:")
T = np.matrix([[0.20, 0.30, 0.05, 0.06, 0.10, 0.04, 0.05, 0.20],
               [0.10, 0.40, 0.05, 0.00, 0.30, 0.05, 0.01, 0.09],
               [0.05, 0.60, 0.20, 0.02, 0.01, 0.04, 0.08, 0.00],
               [0.20, 0.20, 0.04, 0.07, 0.09, 0.30, 0.05, 0.05],
               [0.00, 0.00, 0.50, 0.08, 0.10, 0.04, 0.08, 0.20],
               [0.05, 0.10, 0.10, 0.06, 0.00, 0.09, 0.40, 0.20],
               [0.30, 0.07, 0.10, 0.06, 0.07, 0.15, 0.05, 0.20],
               [0.25, 0.05, 0.40, 0.07, 0.10, 0.03, 0.00, 0.10]])
print(T, '\n')


#Initial State settings

initial_state = config.get('initial state', 'state')
IS = functions.initialstate(initial_state)
print("Initial state: ", initial_state)
I = np.matrix([IS])


#Stationary distribution calculation

number_steps = config.get('number of steps', 'steps') 
number_steps = int(number_steps) - 2
A = functions.stat_distr(T, I, IS, number_steps)
print("\nStationary distribution:")
print(A[len(A)-1]) #the stationary distribution is the last element of A 


#Probabilities calculation

B = A.transpose()
print("\nProbabilities to reach a state at a specific step:")
print("\nState A:", B[0])
print("\nState B:", B[1])
print("\nState C:", B[2])  
print("\nState D:", B[3])  
print("\nState E:", B[4])  
print("\nState F:", B[5])  
print("\nState G:", B[6])  
print("\nState H:", B[7]) 


























