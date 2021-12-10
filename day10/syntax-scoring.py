from functools import reduce

with open("day10/input") as f:
    lines = list(map(str.strip, f.readlines()))

symbols = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

def part_one():
    illegal = {symbol:0 for symbol in symbols.values()}

    for line in lines:
        stack = []
        for symbol in line:
            if symbol in symbols:
                stack.append(symbol)
            else:
                if symbol != symbols[stack[-1]]:
                    illegal[symbol] += 1
                    break
                stack.pop()

    print(illegal[")"] * 3 + illegal["]"] * 57 +
          illegal["}"] * 1197 + illegal[">"] * 25137)

def part_two():
    closing_values = dict(zip(symbols.values(), range(1, 5)))
    scores = []

    for line in lines:
        stack = []
        legal = True
        for symbol in line:
            if symbol in symbols:
                stack.append(symbol)
            else:
                if symbol != symbols[stack[-1]]:
                    legal = False
                    break
                stack.pop()
        if legal:
            scores.append(reduce(lambda a,v: a * 5 + v,
                                 [int(closing_values[_]) for _
                                  in [symbols[symbol] for symbol in stack][::-1]]))

    print(sorted(scores)[len(scores) // 2])

part_one()
part_two()
