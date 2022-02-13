# Simulation of a discrete-time Markov process 
Markov processes are stochastic models which consist in a sequence of events in which the probability of the next event depends only on the state of the current one; 
specifically, this phenomenon is called the memoryless property, also known as the Markov property. Markov processes are important because they are applied to many topics, 
i. e. queues of people arriving at a specific place, currency exchange rates and dynamics of animal population. 
In particular, in this project will be considered a discrete-time Markov chain (DTMC), which is characterized by a countably infinite sequence, in which the system 
moves from state to state at discrete time steps.

The system is defined by 8 states (A, B, C, D, E, F, G, H) and a 8x8 transition matrix T. If the initial distribution ![mu0](https://latex.codecogs.com/gif.latex?%5Cmu%5E0)
and T are known, all the distributions ![muk](https://latex.codecogs.com/gif.latex?%5Cmu%5E1%2C%20%5Cmu%5E2%2C%20...%2C%20%5Cmu%5Ek) of the Markov 
chain can be obtained  by computing a matrix multiplication:

![matrmult](https://latex.codecogs.com/gif.latex?%5Cmu%5En%20%3D%20%5Cmu%5E0%20T%5En)

Markov chains have another property: they reveal an asymptotic behaviour for long-term processes. Hence, for the distribution ![pi](https://latex.codecogs.com/gif.latex?%5Cpi) 
which is stationary for T, we have: 

![statdistr](https://latex.codecogs.com/gif.latex?%5Cmu%5En%20%5Crightarrow%20%5Cpi)

Moreover, the chain can be represented by a random walk, a sequence of selected states which, from a starting point, at every step it selects a neighbour at random and 
moves there. This procedure is repeated until a termination condition is verified.  








