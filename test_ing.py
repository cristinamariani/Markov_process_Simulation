import numpy as np
import Functions
import pytest


#"initialstate" function testing

# test 1: tests that the output is the expected value
def test_initialstate_1():
    IS = np.array([0, 0, 1, 0, 0, 0, 0, 0])
    assert np.array_equal(Functions.initialstate('C'),IS)

# test 2: tests that ValueError is raised when the input is not chosen among {A, B, C, D, E, F, G, H}    
def test_initialstate_2():     
    with pytest.raises(ValueError):
        Functions.initialstate('abc')
        Functions.initialstate(123) 
            
    
   
    







