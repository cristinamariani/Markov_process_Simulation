import numpy as np
import Functions
import pytest
#from Simulation import A#, T#, I, IS #, number_steps

#"initialstate" function testing

# test 1: tests that the output is the expected value
def test_initialstate_1():
    IS = np.array([0, 0, 1, 0, 0, 0, 0, 0])
    assert np.array_equal(Functions.initialstate('C'), IS)

# test 2: tests that ValueError is raised when the input is not chosen among {A, B, C, D, E, F, G, H}    
def test_initialstate_2():     
    with pytest.raises(ValueError):
        Functions.initialstate('abc')
        Functions.initialstate(123) 
            
    
#"stat_distr" function testing 

# test 1: tests that ValueError is raised when the number of steps is <10
def test_stat_distr_1():
    
    T = np.matrix([[0.20, 0.30, 0.05, 0.06, 0.10, 0.04, 0.05, 0.20],
                   [0.10, 0.40, 0.05, 0.00, 0.30, 0.05, 0.01, 0.09],
                   [0.05, 0.60, 0.20, 0.02, 0.01, 0.04, 0.08, 0.00],
                   [0.20, 0.20, 0.04, 0.07, 0.09, 0.30, 0.05, 0.05],
                   [0.00, 0.00, 0.50, 0.08, 0.10, 0.04, 0.08, 0.20],
                   [0.05, 0.10, 0.10, 0.06, 0.00, 0.09, 0.40, 0.20],
                   [0.30, 0.07, 0.10, 0.06, 0.07, 0.15, 0.05, 0.20],
                   [0.25, 0.05, 0.40, 0.07, 0.10, 0.03, 0.00, 0.10]])
    
    IS = np.array([1, 0, 0, 0, 0, 0, 0, 0])
    I = np.matrix([IS])
    number_steps = 5
       
    with pytest.raises(ValueError):
        Functions.stat_distr(T, I, IS, number_steps)







