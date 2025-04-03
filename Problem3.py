import numpy as np
import matplotlib.pyplot as plt

# 8-Puzzle
class Puzzle8:
    def __init__(self):
        self.goal = np.array([1,2,3,4,5,6,7,8,0])
    
    def manhattan(self, state):
        return sum(abs(i//3 - (num-1)//3) + abs(i%3 - (num-1)%3) for i, num in enumerate(state) if num != 0)

    def solve(self, iterations=1000):
        best = []
        current_best = float('inf')
        for _ in range(iterations):
            state = self.goal.copy()
            np.random.shuffle(state)
            cost = self.manhattan(state)
            while True:
                neighbors = []
                zero = np.where(state == 0)[0][0]
                for d in [-3, -1, 1, 3]:
                    if 0 <= zero + d < 9 and (d != -1 or zero %3 !=0) and (d !=1 or zero%3 !=2):
                        neighbor = state.copy()
                        neighbor[zero], neighbor[zero+d] = neighbor[zero+d], neighbor[zero]
                        neighbors.append(neighbor)
                if not neighbors:
                    break
                costs = [self.manhattan(n) for n in neighbors]
                min_cost = min(costs)
                if min_cost >= cost:
                    break
                state = neighbors[np.argmin(costs)]
                cost = min_cost
            if cost < current_best:
                current_best = cost
            best.append(current_best)
        plt.plot(best)
        plt.show()

Puzzle8().solve()

# 8-Queens
class Queens8:
    def conflicts(self, state):
        return sum(abs(i-j) == abs(state[i]-state[j]) or state[i]==state[j] for i in range(8) for j in range(i+1,8))

    def solve(self, iterations=1000):
        best = []
        current_best = float('inf')
        for _ in range(iterations):
            state = np.random.permutation(8)
            cost = self.conflicts(state)
            while True:
                neighbors = []
                for col in range(8):
                    for row in range(8):
                        if row != state[col]:
                            neighbor = state.copy()
                            neighbor[col] = row
                            neighbors.append(neighbor)
                if not neighbors:
                    break
                costs = [self.conflicts(n) for n in neighbors]
                min_cost = min(costs)
                if min_cost >= cost:
                    break
                state = neighbors[np.argmin(costs)]
                cost = min_cost
            if cost < current_best:
                current_best = cost
            best.append(current_best)
        plt.plot(best)
        plt.show()

Queens8().solve()