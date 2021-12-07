import numpy as np

with open("day07/input") as f:
    crabs = np.array(list(map(int, f.read().split(","))))

def count_fuel(target, incremental=False):
    print(sum(map(lambda crab: (sum(range(1, abs(crab - target) + 1)) if incremental
                                else abs(crab - target)),
                   crabs)))

count_fuel(int(np.median(crabs)))
count_fuel(int(crabs.mean()), incremental=True)
