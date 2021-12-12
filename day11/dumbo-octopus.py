from itertools import product

input = """7232374314
8531113786
3411787828
5482241344
5856827742
7614532764
5311321758
1255116187
5821277714
2623834788"""

octopi_initial = [list(map(int, _)) for _ in input.splitlines()]
positions = list(product(range(10), repeat=2))
directions = [(1, 0), (0, 1), (-1, 0), (0, -1),
              (1, 1), (1, -1), (-1, 1), (-1, -1)]

def neighbors(x, y):
    points = set()
    for mx, my in directions:
        xx = x + mx
        yy = y + my
        if 0 > xx or xx > 9 or 0 > yy or yy > 9:
            continue
        points.add((xx, yy))
    return points

def step(octo):
    overflow = set()
    flashed = 0
    for x, y in positions:
        octo[y][x] += 1
        if octo[y][x] == 10:
            overflow.add((x, y))
    while overflow:
        flashed += 1
        xx, yy = overflow.pop()
        for x, y in neighbors(xx, yy):
            octo[y][x] += 1
            if octo[y][x] == 10:
                overflow.add((x, y))
    for x, y in positions:
        if octo[y][x] > 9:
            octo[y][x] = 0
    return flashed

def part_one(octopi):
    print(sum(map(lambda _: step(octopi), range(100))))

def part_two(octopi):
    i = 0
    while True:
        i += 1
        if step(octopi) == len(positions):
            print(i)
            break

part_one(list(map(list, octopi_initial)))
part_two(list(map(list, octopi_initial)))
