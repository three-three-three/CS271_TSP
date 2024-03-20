import matplotlib.pyplot as plt
import os

# input params
instances = [
    "30", "35", "40", "45", "50",
]

# results of SA and DP
sa_dis = [
    1161.664, 1372.473, 1443.46, 1593.488, 1708.934,
]

sa_time = [
    0.649, 0.632, 0.955, 0.733, 0.792,
]

bnb_dis = [
    1361.87, 1613.25, 1754.56, 2119.62, 2227.57
]

bnb_time = [
    0.002, 0.018, 0.075, 0.604, 3.617, 51.865, 61.215, 800.252
]

sa_bnb_distance_ratio = [sa / bnb for sa, bnb in zip(sa_dis, bnb_dis)]

plt.figure(figsize=(10, 6))

# distance comparision
# plt.subplot(1, 1, 1)
plt.plot(instances, sa_bnb_distance_ratio, label='SA/BNB Distance Ratio', marker='^', linestyle='--')
plt.title('Distance Comparison')
plt.xlabel('Instance (n)')
plt.ylabel('SA-BNB Ratio')
plt.legend()

# time comparision
# plt.subplot(1, 2, 2)
# plt.plot(instances, sa_time, label='Simulated Annealing Time', marker='o')
# plt.plot(instances, bnb_time, label='Branch and Bound Time', marker='^')
# plt.title('Time Comparison')
# plt.xlabel('Instance (n)')
# plt.ylabel('Time (seconds)')
# plt.yscale('log')  
# plt.legend()

plt.tight_layout()

output_dir = 'Output_Fig'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

plt.savefig('Output_Fig/Figure_SA_BNB_30-50.png')

plt.show()