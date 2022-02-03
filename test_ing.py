import numpy as np
import Functions
import pytest
import configparser
import json


config = configparser.ConfigParser()
config.read('Configuration.txt')


#Variables that are used in testing functions 

#Transition Matrix
T = config.get('transition matrix', 'T')
T = json.loads(T)
T = np.matrix(T)

#Values for number of steps = 10 with initial state 'A' and random seed = 3
IS = np.array([1, 0, 0, 0, 0, 0, 0, 0])
I = np.matrix([IS])
number_steps = 10

A = [[1., 0., 0., 0., 0., 0., 0., 0.],
     [0.2, 0.3, 0.05, 0.06, 0.1, 0.04, 0.05, 0.2],
     [0.1515, 0.2395, 0.1764, 0.0446, 0.1494, 0.0641, 0.0465, 0.128],
     [0.121145, 0.272075, 0.193574, 0.043288, 0.123773, 0.061031, 0.066229,  0.118885],
     [0.1224143, 0.28665888, 0.18227382, 0.04002973, 0.12847049, 0.06312352, 0.06405401, 0.11297525],
     [0.12088458, 0.28520298, 0.18065271, 0.03960897, 0.13229286, 0.06234668, 0.06430044, 0.11471077],
     [0.1207368, 0.28313122, 0.18271473, 0.03985077, 0.13222208, 0.06219364, 0.06406605, 0.11508471],
     [0.12066705, 0.28353075, 0.18310127, 0.03989733, 0.13164207, 0.06219861, 0.06413639, 0.11482653],
     [0.1206785, 0.28390338, 0.18281118, 0.03984418, 0.13168411, 0.06222528, 0.06412926, 0.11472411],
     [0.1206665, 0.28386823, 0.18275225, 0.03983272, 0.13178282, 0.06221676, 0.06412137, 0.11475935],
     [0.1206665, 0.28386823, 0.18275225, 0.03983272, 0.13178282, 0.06221676, 0.06412137, 0.11475935]]

statdistr = np.array([0.1206665, 0.28386823, 0.18275225, 0.03983272, 0.13178282, 0.06221676, 0.06412137, 0.11475935])
states = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
randomwalk = ['A', 'B', 'C', 'B', 'E', 'E', 'C', 'A', 'H', 'B', 'B']


#"initialstate" function testing

# test 1: tests that the output is the expected value
def test_initialstate_1():
    assert np.array_equal(Functions.initialstate('A'), IS)

# test 2: tests that ValueError is raised when the input is not chosen among {A, B, C, D, E, F, G, H}    
def test_initialstate_2():     
    with pytest.raises(ValueError):
        Functions.initialstate('abc')
        Functions.initialstate(123)  
            

#"stat_distr" function testing 

# test 1: tests that the output is the expected value
def test_stat_distr_1():
    func_outcome = Functions.stat_distr(T, I, IS, number_steps)[10]
    assert np.allclose(func_outcome, statdistr)

# test 1: tests that ValueError is raised when the number of steps is <10
def test_stat_distr_2():
    number_steps = 5       
    with pytest.raises(ValueError):
        Functions.stat_distr(T, I, IS, number_steps)


#"rnd_walk" function testing

# test 1: tests that the output is the expected value
def test_rnd_walk_1():
    assert Functions.rnd_walk(A, T, 'A', states, 3) == randomwalk
        



























