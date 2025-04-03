Hill Climbing with Random Restart 
8-puzzle and 8 queens 
8-puzzle: Manhattan distance guides the search towards the goal state. 8-queens: 
Minimizing conflicts improves board state. Random restarts reinitialize the search upon any 
stagnation. Hill climbing with random restarts to escape local optima.  
Problem: Hill climbing trapped in local minima. Added random restarts after 100 iterations 
of no improvements.

Overview of the Approach
1. 8-Puzzle (Manhattan Distance)
The Manhattan Distance heuristic helps guide the search toward the goal state.

If no better move is found within 100 iterations, the board is randomly reset (Random Restart).

2. 8-Queens (Minimizing Conflicts)
The heuristic function counts the number of queens attacking each other.

A queen is moved to the row that results in the fewest conflicts.

If no improvement is made in 100 iterations, the board is randomly reset.
