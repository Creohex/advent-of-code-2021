from functools import reduce

with open("day09/input") as f:
    heightmap = list(map(lambda s: [int(_) for _ in s.strip()], f.readlines()))

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def adjacent(x, y):
    vals = []
    for mx, my in directions:
        xx = x + mx
        yy = y + my
        if (0 > xx or xx >= len(heightmap[y]) or
            0 > yy or yy >= len(heightmap)):
            continue
        vals.append((xx, yy))
    return vals

def part_one():
    lowest = []
    for y in range(len(heightmap)):
        for x in range(len(heightmap[y])):
            val = heightmap[y][x]
            adj = adjacent(x, y)
            if not [(xx,yy) for xx, yy in adj if val >= heightmap[yy][xx]]:
                lowest.append(val)
    print(sum(lowest) + len(lowest))

def part_two():
    basins = []
    visited = []

    def explore_basin(x, y):
        basin = [(x, y)]
        visited.append((x, y))

        while True:
            extension = []
            for xx, yy in basin:
                for adj in adjacent(xx, yy):
                    adjx, adjy = adj
                    if heightmap[adjy][adjx] != 9 and adj not in visited:
                        extension.append(adj)
                        visited.append(adj)
            if extension:
                basin.extend(extension)
            else:
                break
        return basin

    for y in range(len(heightmap)):
        for x in range(len(heightmap[y])):
            if heightmap[y][x] != 9 and (x, y) not in visited:
                basin = explore_basin(x, y)
                basins.append(basin)

    print(reduce(lambda a,b: a * b,
                 sorted([len(b) for b in basins])[-3:]))

part_one()
part_two()
