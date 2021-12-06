with open("day06/input") as f:
    fish = list(map(int, f.read().split(",")))

def breed(fish, days):
    fish = {k: fish.count(k) for k in range(9)}
    for _ in range(days):
        iteration = {k-1: fish[k] for k in range(1, 9)}
        iteration[8] = fish[0]
        iteration[6] += fish[0]
        fish = iteration
    print(sum(fish.values()))

breed(fish, 80)
breed(fish, 256)
