import numpy as np
import Functions
import pytest
import math
import collections


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
IS = np.array([1, 0, 0, 0, 0, 0, 0, 0]) #initial state array
number_steps = 30
statdistr = np.array([0.12066125, 0.28382706, 0.18280321, 0.0398397, 0.13176984, 0.06221281, 0.0641203, 0.11476584])
states = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
randomwalk = ['A', 'B', 'C', 'B', 'E', 'E', 'C', 'A', 'H', 'B', 'B', 'H', 'C', 'C', 'B', 'E', 'C', 'B', 'F', 'G', 'F', 'G', 'A', 'G', 'E', 'C', 'A', 'H', 'C', 'C', 'E']
fake_randomwalk1 = ['B', 'D', 'G', 'G', 'G', 'A', 'G', 'E', 'C']
fake_randomwalk2 = ['A', 'F', 'G', 'F', 'G', 'A', 'H', 'G', 'B']


#"initialstate" function testing

def test_initialstate_1():
    """Test 1: tests that the output is the expected value"""
    assert np.array_equal(Functions.initialstate('A'), IS)    
    
def test_initialstate_2(): 
    """Test 2: tests that ValueError is raised when the input is not chosen among {A, B, C, D, E, F, G, H}"""    
    with pytest.raises(ValueError):
        Functions.initialstate('abc')
        Functions.initialstate(123)  

def test_initialstate_3():
    """Test 3: tests that the output array has 8 elements"""
    assert len(Functions.initialstate('A')) == 8
     
def test_initialstate_4():
    """Test 4: tests that, for different input, the output is different""" 
    assert not np.array_equal(Functions.initialstate('E'),Functions.initialstate('C'))
    
def test_initialstate_5():
    """Test 5: tests that the output array has 1 element equal to 1 and the others equal to 0"""
    assert np.count_nonzero(Functions.initialstate('A')) == 1 #only one element is non-zero
    assert np.count_nonzero(Functions.initialstate('A') == 1) == 1 #the only one non-zero element is 1
            
 
#"stat_distr" function testing 

def test_prob_distr_1():
    """Test 1: tests that the calculated stationary distribution is the expected value"""
    func_outcome = Functions.prob_distr(T, IS, number_steps)[30] 
    assert np.allclose(func_outcome, statdistr)

def test_prob_distr_2():
    """Test 2: tests that the sum of the elements of the stationary distribution array is equal to 1"""
    assert math.isclose(np.sum(Functions.prob_distr(T, IS, number_steps)[30]),1)
 
def test_prob_distr_3():
    """Test 3: tests that for different initial state, the stationary distribution is the same"""
    assert np.array_equal(Functions.prob_distr(T, Functions.initialstate('F'), 100)[100], Functions.prob_distr(T, Functions.initialstate('G'), 100)[100])


#"rnd_walk" function testing

def test_rnd_walk_1():
    """Test 1: tests that the output is the expected value"""
    assert Functions.rnd_walk(number_steps, T, 'A', states, 3) == randomwalk
    
def test_rnd_walk_2():
    """Test 2: tests that the probability distribution of the occurrences of the chain is approximately equal to the stationary distribution"""
    occurrences1 = collections.Counter(Functions.rnd_walk(1001000, T, 'A', states, 7)[-1000000:])
    probdistr1 = []
    probdistr1.append(round(occurrences1['A']/1000000, 2))
    probdistr1.append(round(occurrences1['B']/1000000, 2))
    probdistr1.append(round(occurrences1['C']/1000000, 2))
    probdistr1.append(round(occurrences1['D']/1000000, 2))
    probdistr1.append(round(occurrences1['E']/1000000, 2))
    probdistr1.append(round(occurrences1['F']/1000000, 2))
    probdistr1.append(round(occurrences1['G']/1000000, 2))
    probdistr1.append(round(occurrences1['H']/1000000, 2))
    probdistr1 = np.array(probdistr1)
    assert np.array_equal(probdistr1, np.around(statdistr, 2))    
    #test the same as above but considering a chain generated with a different random seed
    occurrences2 = collections.Counter(Functions.rnd_walk(1001000, T, 'A', states, 1)[-1000000:])
    probdistr2 = []
    probdistr2.append(round(occurrences2['A']/1000000, 2))
    probdistr2.append(round(occurrences2['B']/1000000, 2))
    probdistr2.append(round(occurrences2['C']/1000000, 2))
    probdistr2.append(round(occurrences2['D']/1000000, 2))
    probdistr2.append(round(occurrences2['E']/1000000, 2))
    probdistr2.append(round(occurrences2['F']/1000000, 2))
    probdistr2.append(round(occurrences2['G']/1000000, 2))
    probdistr2.append(round(occurrences2['H']/1000000, 2))
    probdistr2 = np.array(probdistr2)
    assert np.array_equal(probdistr2, np.around(statdistr, 2))
    assert np.array_equal(probdistr1, probdistr2)        


#"check_rnd_walk" function testing

def test_check_rnd_walk1():
    """Test 1: tests that the given random walk does not contain forbidden transitions"""
    assert Functions.check_rnd_walk(Functions.rnd_walk(number_steps, T, 'B', states, 4))   
    assert Functions.check_rnd_walk(Functions.rnd_walk(number_steps, T, 'A', states, 1))
    assert not Functions.check_rnd_walk(fake_randomwalk1)
    assert not Functions.check_rnd_walk(fake_randomwalk2)
























