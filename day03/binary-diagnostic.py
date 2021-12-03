from functools import reduce

with open("day03/input") as f:
    report = list(map(str.strip, f.readlines()))

def handle(acc, value):
    for i in range(len(value)):
        acc[i][int(value[i])] += 1
    return acc

def process(data):
    return reduce(lambda a,v: handle(a, v), data,
                  [[0, 0] for _ in range(len(data[0]))])

def part_one():
    def get_rating(seq, callable):
        return int("".join(str(callable(enumerate(c), key=lambda _: _[1])[0])
                           for c in process(seq)), 2)
    print(get_rating(report, max) * get_rating(report, min))

def part_two():
    def get_rating(seq, callable):
        for i in range(len(seq[0])):
            char_map = process(seq)
            char = str(callable([0, 1]) if char_map[i][0] == char_map[i][1]
                       else callable(enumerate(char_map[i]), key=lambda _: _[1])[0])
            seq = list(filter(lambda n: n[i] == char, seq))
            if len(seq) == 1:
                return int("".join(seq[0]), 2)
    print(get_rating(report, max) * get_rating(report, min))

part_one()
part_two()
