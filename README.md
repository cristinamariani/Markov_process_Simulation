# Eight-states discrete-time Markov process 
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

## Simulation of an eight-states discrete-time Markov process

This code has the purpose to simulate an 8-state discrete-time Markov process and to analyze its behaviour. In particular, the characteristics I focused on are the calculation
of the stationary distribution and the generation of an example of a possible random walk.
I split the project in four files: 

* [Configuration.txt](https://github.com/cristinamariani/Markov_process_Simulation/blob/master/Configuration.txt) is provided with the transition matrix and the initial settings for starting the simulation: the initial state and the number of steps.
* The file [Functions.py](https://github.com/cristinamariani/Markov_process_Simulation/blob/master/Functions.py) contains all the functions needed for the simulation: the first function returns an array which identifies the initial state; the second function performs the matrix multiplication and returns an array that contains all the 
calculated distributions: for a minimum number of steps equal to 10, the stationary distribution is the last element of that array. The third function has the role of plotting
the probabilities to reach one state at every step, whereas the fourth function is in charge of generating an example of a possible random walk "traveled" by the system
during the process.
* The file [Simulation.py](https://github.com/cristinamariani/Markov_process_Simulation/blob/master/Simulation.py) contains all the instructions for running the simulation: 
here, the system in initialized by importing the configuration file thanks to the ConfigParser library; moreover, all the functions from Functions.py are exploited. This 
file allows the calculation of the stationary distribution and of the probabilities to reach one state at every step. Furthermore, there are the plotting of those probabilities versus the number of steps and the construction of a simulated random walk, which is built by exploiting the random library and an arbitrary random seed. As expected, the stability of the process is reached and the stationary distribution is the same independently on the initial state. 
* with [test_ing.py](https://github.com/cristinamariani/Markov_process_Simulation/blob/master/test_ing.py) I could test all the functions in order to verify them to work
properly.

To start the simulation, the user can modify the configuration file to choose the initial state and the number of steps; I selected ![A](https://latex.codecogs.com/gif.latex?A) as initial state and number of steps equal to 30 as default settings. After this, the user simply has to run the simulation file by writing on the command line: 

```bash
python Simulation.py
```




