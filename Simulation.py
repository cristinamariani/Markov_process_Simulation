import numpy as np 
import Functions
import configparser
import json


config = configparser.ConfigParser()
config.read('Configuration.txt')


print("\n")
print("****************************************************")
print("Eight-state Discrete-time Markov process Simulation")
print("****************************************************")


#Transition Matrix

print("\nTransition matrix:")
T = config.get('transition matrix', 'T')
T = json.loads(T)
T = np.matrix(T)
print(T, '\n')


#Initial State settings

initial_state = config.get('initial state', 'state')
IS = Functions.initialstate(initial_state)
print("Initial state: ", initial_state)
I = np.matrix([IS])


#Stationary distribution calculation

number_steps = config.get('number of steps', 'steps') 
number_steps = int(number_steps)
A = Functions.stat_distr(T, I, IS, number_steps)
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


#Plot

Functions.plot_func(A, B) 


#Random walk generation

states = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
seed = 3 #random seed
path = Functions.rnd_walk(A, T, initial_state, states, seed)
print("\nRandom walk example:")
print(path)

 



















