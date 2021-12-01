
def count_increases(seq):
    print(list(map(lambda p: p[1] > p[0], zip(seq, seq[1:]))).count(True))

with open("day01/input") as f:
    sequence = list(map(int, f.readlines()))

count_increases(sequence)
count_increases(list(map(sum, zip(sequence, sequence[1:], sequence[2:]))))
