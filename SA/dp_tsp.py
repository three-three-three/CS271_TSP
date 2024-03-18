import time
import numpy as np

# Parse distance matrix
def read_distance_matrix(filename):
    with open(filename) as f:
        n = int(next(f).strip())  
        D = [[float(x) for x in line.split()] for line in f]
    return np.array(D)


# Generator for combinations of a specific length from the iterable.
def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)


# Held-Karp algorithm
def held_karp(D):
    n = len(D)
    C = {}
    for k in range(1, n):
        C[(1 << k, k)] = (D[0][k], 0)
    for subset_size in range(2, n):
        for subset in combinations(range(1, n), subset_size):
            bits = 0
            for bit in subset:
                bits |= 1 << bit
            for k in subset:
                prev = bits & ~(1 << k)
                res = []
                for m in subset:
                    if m == 0 or m == k:
                        continue
                    res.append((C[(prev, m)][0] + D[m][k], m))
                C[(bits, k)] = min(res)
    bits = (2 ** n - 1) - 1  # Bitmask for all cities except the starting city
    res = []
    for k in range(1, n):
        res.append((C[(bits, k)][0] + D[k][0], k))
    opt, parent = min(res)

    # Reconstructing the path
    path = [0]
    for i in range(n - 1):
        path.append(parent)
        new_bits = bits & ~(1 << parent)
        _, parent = C[(bits, parent)]
        bits = new_bits
    path.append(0)

    return opt, path

# main
filenames = [
        "tsp-problem-7-20-50-10-1.txt",
        "tsp-problem-8-20-50-10-1.txt",
        "tsp-problem-9-20-50-10-1.txt",
        "tsp-problem-10-20-50-10-1.txt",
        "tsp-problem-11-20-50-10-1.txt",
        "tsp-problem-12-20-50-10-1.txt",
        "tsp-problem-13-20-50-10-1.txt",
        "tsp-problem-14-20-50-10-1.txt",
    ]

ans = []
times = []

for filename in filenames:
    start_time = time.time()
    filename = f"Archive/{filename}"
    D = read_distance_matrix(filename)
    # Held-Karp
    opt, path = held_karp(D)
    elapsed_time = time.time() - start_time
    ans.append(round(opt, 3))
    times.append(round(elapsed_time, 3))

    print(f"Filename: {filename}")
    print("Opt solution:", path)
    print("Total distance:", opt)
    print(f"Elapsed time: {elapsed_time:.2f} seconds")
    print("-" * 40)
print(ans)
print(times)
