import matplotlib.pyplot as plt

# input params
instances = [
    "10-20-1", "10-20-2", "10-20-3", "10-20-4", "10-20-5",
    "20-80-1", "20-80-2", "20-80-3", "20-80-4", "20-80-5"
]

# results of SA and DP
sa_dis = [
    416.36128132869413, 461.45983481234776, 394.0168501214223, 410.13359158602395, 383.4348568129652,
    736.4222049596809, 748.3661549372592, 749.6789470441566, 741.5588836858417, 773.1699839076126
]

sa_time = [
    0.43, 0.44, 0.33, 0.33, 0.34,
    0.58, 0.48, 0.59, 0.47, 0.45
]

dp_dis = [
    414.0759504298615, 461.1009322587407, 394.01685012142235, 408.81016628921327, 377.9677436696582, 
    699.6214041635594, 726.190430619759, 708.5032657566356, 714.1858275019719, 758.6837434169134
]

dp_time = [
    0.01, 0.00, 0.01, 0.01, 0.00,
    22.90, 23.05, 23.51, 24.01, 24.47,
]

plt.figure(figsize=(14, 6))

# distance comparision
plt.subplot(1, 2, 1)
plt.plot(instances, sa_dis, label='Simulated Annealing Distance', marker='o')
plt.plot(instances, dp_dis, label='Dynamic Programming Distance', marker='x')
plt.title('Distance Comparison')
plt.xlabel('Instance (n-k-i)')
plt.ylabel('Distance')
plt.xticks(rotation=45) 
plt.legend()

# time comparision
plt.subplot(1, 2, 2)
plt.plot(instances, sa_time, label='Simulated Annealing Time', marker='o')
plt.plot(instances, dp_time, label='Dynamic Programming Time', marker='x')
plt.title('Time Comparison')
plt.xlabel('Instance (n-k-i)')
plt.ylabel('Time (seconds)')
plt.yscale('log')  
plt.xticks(rotation=45)
plt.legend()

plt.tight_layout()
plt.show()

