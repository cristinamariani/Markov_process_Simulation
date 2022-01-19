import numpy as np
import Functions
import pytest


def test_initialstate():
    IS = np.array([0, 0, 1, 0, 0, 0, 0, 0])
    assert np.array_equal(Functions.initialstate('C'),IS)
    
    
    
    
    
    
    
    







