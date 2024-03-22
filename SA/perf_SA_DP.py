import matplotlib.pyplot as plt
import os

# input params
instances = [
    "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"
]

# results of SA and DP
sa_dis = [
    359.64, 386.071, 441.787, 506.963, 553.683, 570.84, 499.171, 637.4, 770.113, 739.32, 748.764
]

sa_time = [
    0.402, 0.354, 0.37, 0.386, 0.389, 0.4, 0.404, 0.419, 0.838, 0.46, 0.488
]

dp_dis = [
    359.64, 384.461, 431.917, 505.508, 553.683, 543.335, 487.678, 616.068, 764.034, 728.042, 699.268
]

dp_time = [
    0.005, 0.017, 0.025, 0.06, 0.137, 0.299, 0.7, 1.627, 4.29, 10.583, 24.257
]

sa_dp_distance_ratio = [sa / dp for sa, dp in zip(sa_dis, dp_dis)]

plt.figure(figsize=(14, 6))

# distance comparision
plt.subplot(1, 2, 1)
plt.plot(instances, sa_dp_distance_ratio, label='SA/DP Distance Ratio', marker='^', linestyle='--')
plt.title('Distance Comparison')
plt.xlabel('Instance (n)')
plt.ylabel('SA-DP Ratio')
plt.legend()

# time comparision
plt.subplot(1, 2, 2)
plt.plot(instances, sa_time, label='Simulated Annealing Time', marker='o')
plt.plot(instances, dp_time, label='Dynamic Programming Time', marker='x')
plt.title('Time Comparison')
plt.xlabel('Instance (n)')
plt.ylabel('Time (seconds)')
plt.yscale('log')  
plt.legend()

plt.tight_layout()

output_dir = 'Output_Fig'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

plt.savefig('Output_Fig/Figure_SA_DP_7-14.png')

plt.show()

