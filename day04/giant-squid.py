with open("day04/input") as f:
    lines = f.readlines()
numbers = list(map(int, lines.pop(0).split(",")))
cards = [list(map(lambda row: list(map(int, row.split())), lines[_ + 1:_ + 6]))
         for _ in range(0, len(lines), 6)]

def is_bingo(card):
    return any(filter(lambda l: sum(l) == -5, card + list(zip(*card))))

def bingo(last):
    cards_won = []
    for n in numbers:
        for i, card in enumerate(cards):
            for row in card:
                if n in row:
                    row[row.index(n)] = -1
            if i not in cards_won and is_bingo(card):
                cards_won.append(i)
                if not last or len(cards_won) == len(cards):
                    return n * sum(map(lambda row: sum(filter(lambda v: v > 0, row)),
                                       card))

print(bingo(False))
print(bingo(True))
