import numpy as np
import random
import math
import time

# Parse distance matrix
def read_distance_matrix(filename):
    with open(filename) as f:
        next(f)  
        D = [list(map(float, line.split())) for line in f if line.strip()]
    return np.array(D, dtype=float)


# Generates a neighbor solution by swapping two randomly selected locations.
def generate_random_neighbor(solution):
    i, j = random.sample(range(len(solution)), 2)  # choose 2 locations randomly
    neighbor = solution.copy()
    neighbor[i], neighbor[j] = neighbor[j], neighbor[i]  # swap
    return neighbor


# Calculates the distance of a given TSP solution.
def tsp_distance(D, solution):
    sum_distance = sum(D[solution[i], solution[i+1]] for i in range(len(solution)-1))
    sum_distance += D[solution[-1], solution[0]]
    return sum_distance


# Simulated Annealing algorithm
def simulated_annealing(D, T_initial=10000, T_min=1, alpha=0.99, MAX_ITER=100):
    n = len(D)
    current_solution = list(range(n))
    random.shuffle(current_solution)
    current_cost = tsp_distance(D, current_solution)
    
    # corresponding to pseudo code
    T = T_initial # Start temperature
    while T > T_min: # Continue until cooling down to minimum temperature
        for _ in range(MAX_ITER):
            neighbor = generate_random_neighbor(current_solution)
            neighbor_cost = tsp_distance(D, neighbor)
            cost_difference = neighbor_cost - current_cost
            
            # Accept neighbor if it's better or based on probability
            if cost_difference < 0 or random.random() < math.exp(-cost_difference / T):
                current_solution = neighbor
                current_cost = neighbor_cost
                
        T *= alpha # Cool down
    
    return current_solution, current_cost


if __name__ == "__main__":
    filenames = [
        "tsp-problem-10-20-50-10-1.txt",
        "tsp-problem-11-20-50-10-1.txt",
        "tsp-problem-12-20-50-10-1.txt",
        "tsp-problem-13-20-50-10-1.txt",
        "tsp-problem-14-20-50-10-1.txt",
        "tsp-problem-15-20-50-10-1.txt",
        "tsp-problem-16-20-50-10-1.txt",
        "tsp-problem-17-20-50-10-1.txt",
        "tsp-problem-18-20-50-10-1.txt",
        "tsp-problem-19-20-50-10-1.txt",
        "tsp-problem-20-20-50-10-1.txt",
    ]
    
    ans = []
    times = []

    for filename in filenames:
        start_time = time.time()
        filename = f"Archive/{filename}"
        D = read_distance_matrix(filename)

        solution, distance = simulated_annealing(D)
        elapsed_time = time.time() - start_time # Calculate elapsed time
        times.append(round(elapsed_time, 3))

        distance_rounded = round(distance, 3)
        ans.append(distance_rounded)

        print(f"Filename: {filename}")
        print("Final solution:", solution)
        print("Total distance:", distance_rounded)
        print(f"Elapsed time: {elapsed_time:.2f} seconds")
        print("-" * 40)  
    
    print(ans)
    print(times)

