# CSC370-HW1

Authors: Caroline Sigl and Lindy Bustabad, CSC370

Contains eightpuzzle.py class that creates sliding 8-puzzle with initial state formed by reverse walking legal slides from a valid arrangement. RANDOMIZATION_NUMBER global variable: determines maximum number of reverse-walks to take from goal state to reach initial state.

Contains a_star.py module that implements A* algorithm to solve sliding 8-puzzle. Includes h1 - Hamming distance heuristic, h2 - Manhattan distance heuristic, h3 - Relaxed Adjacency heuristic. NUMBER_OF_TRIALS global variable: determines number of trials to run.

To run code: 
```
python3 a_star.py
```

Exports CSV titled "3_heuristics.csv" containing nodes generated and effective branching factor data for three heuristic functions.


