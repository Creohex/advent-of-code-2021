from functools import reduce

with open("day02/input") as f:
    commands = list(map(lambda _: (_[0], int(_[1])), map(str.split, f.readlines())))

def handle(acc, cmd, units, extended):
    if cmd == "forward":
        acc["x"] += units
        if extended:
            acc["y"] += acc["aim"] * units
    elif cmd == "up":
        acc["aim" if extended else "y"] -= units
    elif cmd == "down":
        acc["aim" if extended else "y"] += units
    return acc

def solve(extended):
    coords = reduce(lambda a,v: handle(a, v[0], v[1], extended),
                    commands, {"x": 0, "y": 0, "aim": 0})
    print(coords["x"] * coords["y"])

solve(False)
solve(True)
