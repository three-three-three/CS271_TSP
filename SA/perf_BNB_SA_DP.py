import matplotlib.pyplot as plt
import os

# input params
instances = [
    "7", "8", "9", "10", "11", "12", "13", "14"
]

# results of SA and DP
sa_dis = [
    285.402, 321.177, 319.828, 359.64, 387.497, 431.917, 506.963, 553.683
]

sa_time = [
    0.309, 0.341, 0.322, 0.331, 0.346, 0.359, 0.377, 0.388
]

bnb_dis = [
    285.402, 321.177, 319.828,  359.64, 384.461, 431.917,  505.508, 553.683
]

bnb_time = [
    0.002, 0.018, 0.075, 0.604, 3.617, 51.865, 61.215, 800.252
]

dp_dis = [
    285.402, 321.177, 319.828, 359.64, 384.461, 431.917, 505.508, 553.683
]

dp_time = [
    1e-6, 0.001, 0.002, 0.005, 0.011, 0.041, 0.061, 0.136
]

sa_dp_distance_ratio = [sa / dp for sa, dp in zip(sa_dis, dp_dis)]
bnb_dp_distance_ratio = [bnb / dp for bnb, dp in zip(bnb_dis, dp_dis)]

plt.figure(figsize=(14, 6))

# distance comparision
plt.subplot(1, 2, 1)
plt.plot(instances, sa_dp_distance_ratio, label='SA/DP Distance Ratio', marker='^', linestyle='--')
plt.plot(instances, bnb_dp_distance_ratio, label='BNB/DP Distance Ratio')
plt.title('Distance Comparison')
plt.xlabel('Instance (n)')
plt.ylabel('SA-DP and BNB-DP Ratio')
plt.legend()

# time comparision
plt.subplot(1, 2, 2)
plt.plot(instances, sa_time, label='Simulated Annealing Time', marker='o')
plt.plot(instances, dp_time, label='Dynamic Programming Time', marker='x')
plt.plot(instances, bnb_time, label='Branch and Bound Time', marker='^')
plt.title('Time Comparison')
plt.xlabel('Instance (n)')
plt.ylabel('Time (seconds)')
plt.yscale('log')  
plt.legend()

plt.tight_layout()

output_dir = 'Output_Fig'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

plt.savefig('Output_Fig/Figure_SA_BNB_DP_7-14.png')

plt.show()