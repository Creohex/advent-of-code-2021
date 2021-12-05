with open("day05/input") as f:
    lines = [[list(map(int, route.split(","))) for route in line.split(" -> ")]
             for line in f.readlines()]

def calculate_overlaps(count_diagonals=False):
    coords = {}
    for f,t in lines:
        if f[0] != t[0] and f[1] != t[1]:
            if not count_diagonals:
                continue
            x_min = min(f[0], t[0])
            y_min = min(f[1], t[1])
            x = list(range(x_min, x_min + abs(f[0] - t[0]) + 1))
            y = list(range(y_min, y_min + abs(f[1] - t[1]) + 1))
            points = zip(x if f[0] < t[0] else reversed(x),
                         y if f[1] < t[1] else reversed(y))
        else:
            xx = [f[0], t[0]]
            yy = [f[1], t[1]]
            points = (((_, f[1]) for _ in range(min(xx), max(xx) + 1)) if f[1] == t[1]
                      else ((f[0], _) for _ in range(min(yy), max(yy) + 1)))

        for p in points:
            coords[p] = coords[p] + 1 if p in coords else 1

    print(len([_ for _ in coords.values() if _ > 1]))

calculate_overlaps()
calculate_overlaps(count_diagonals=True)
