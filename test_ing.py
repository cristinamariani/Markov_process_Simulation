import numpy as np
import Functions
import pytest
import math


#Variables used in testing functions 

#Transition Matrix
T = np.matrix([[ 0.2,  0.3, 0.05, 0.06,  0.1, 0.04, 0.05,  0.2],
               [ 0.1,  0.4, 0.05,    0,  0.3, 0.05, 0.01, 0.09],
               [0.05,  0.6,  0.2, 0.02, 0.01, 0.04, 0.08,    0],
               [ 0.2,  0.2, 0.04, 0.07, 0.09,  0.3, 0.05, 0.05],
               [   0,    0,  0.5, 0.08,  0.1, 0.04, 0.08,  0.2],
               [0.05,  0.1,  0.1, 0.06,    0, 0.09,  0.4,  0.2],
               [ 0.3, 0.07,  0.1, 0.06, 0.07, 0.15, 0.05,  0.2],
               [0.25, 0.05,  0.4, 0.07,  0.1, 0.03,    0,  0.1]])

#Values for number of steps = 30 with initial state 'A' and random seed = 3
IS = np.array([1, 0, 0, 0, 0, 0, 0, 0])
number_steps = 30
statdistr = np.array([0.12066125, 0.28382706, 0.18280321, 0.0398397, 0.13176984, 0.06221281, 0.0641203, 0.11476584])
states = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
randomwalk = ['A', 'B', 'C', 'B', 'E', 'E', 'C', 'A', 'H', 'B', 'B', 'H', 'C', 'C', 'B', 'E', 'C', 'B', 'F', 'G', 'F', 'G', 'A', 'G', 'E', 'C', 'A', 'H', 'C', 'C', 'E']


#"initialstate" function testing

# test 1: tests that the output is the expected value
def test_initialstate_1():
    assert np.array_equal(Functions.initialstate('A'), IS)    

# test 2: tests that ValueError is raised when the input is not chosen among {A, B, C, D, E, F, G, H}    
def test_initialstate_2():     
    with pytest.raises(ValueError):
        Functions.initialstate('abc')
        Functions.initialstate(123)  

# test 3: tests that the output array has 8 elements
def test_initialstate_3():
    assert len(Functions.initialstate('A')) == 8
    
# test 4: tests that, for different input, the output is different  
def test_initialstate_4():
    assert not np.array_equal(Functions.initialstate('E'),Functions.initialstate('C'))
    
# test 5: tests that the output array has 1 element equal to 1 and the others equal to 0
def test_initialstate_5():
    assert np.count_nonzero(Functions.initialstate('A')) == 1 #only one element is non-zero
    assert np.count_nonzero(Functions.initialstate('A') == 1) == 1 #the only one non-zero element is 1
            
 
#"stat_distr" function testing 

# test 1: tests that the calculated stationary distribution is the expected value
def test_prob_distr_1():
    func_outcome = Functions.prob_distr(T, IS, number_steps)[30] 
    assert np.allclose(func_outcome, statdistr)

# test 2: tests that the sum of the elements of the stationary distribution array is equal to 1
def test_prob_distr_2():
    assert math.isclose(np.sum(Functions.prob_distr(T, IS, number_steps)[30]),1)

# test 4: tests that for different initial state, the stationary distribution is the same  
def test_prob_distr_4():
    assert np.array_equal(Functions.prob_distr(T, Functions.initialstate('F'), 100)[100], Functions.prob_distr(T, Functions.initialstate('G'), 100)[100])


#"rnd_walk" function testing

# test 1: tests that the output is the expected value
def test_rnd_walk_1():
    assert Functions.rnd_walk(number_steps, T, 'A', states, 3) == randomwalk
        

    
    
























