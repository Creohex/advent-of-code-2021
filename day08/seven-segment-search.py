import random

with open("day08/input") as f:
    input = f.readlines()

def part_one():
    target_lenghts = [2, 3, 4, 7]
    print(sum(map(lambda seg: len([_ for _ in seg if len(_) in target_lenghts]),
                  map(lambda line: line.split("|")[1].split(),
                      input))))

def part_two():
    def decode(line):
        while True:
            parts = line.split("|")
            patterns = list(map(set, parts[0].split()))
            code = list(map(set, parts[1].split()))
            fives = []  # 2,3,5
            sixes = []  # 0,6,9

            code_map = {chr(97 + _):None for _ in range(7)}
            digits = {d:set() for d in range(10)}
            for segments in patterns:
                if len(segments) == 2:
                    digits[1] = segments
                elif len(segments) == 3:
                    digits[7] = segments
                elif len(segments) == 4:
                    digits[4] = segments
                elif len(segments) == 5:
                    fives.append(segments)
                elif len(segments) == 6:
                    sixes.append(segments)
                elif len(segments) == 7:
                    digits[8] = segments

            for five in fives:
                if len(five.difference(digits[4].union(digits[7]))) == 2:
                    digits[2] = five
                elif len(five.difference(digits[1])) == 3:
                    digits[3] == five
                elif len(five.difference(digits[1])) == 4:
                    digits[5] = five

            for six in sixes:
                if len(six.difference(digits[7])) == 4:
                    digits[6] = six
                elif len(six.difference(digits[4])) == 3:
                    digits[0] = six
                elif len(six.difference(digits[4])) == 2:
                    digits[9] = six

            code_map["a"] = digits[7].difference(digits[1]).pop()
            code_map["d"] = digits[4].difference(digits[0]).pop()
            code_map["e"] = digits[8].difference(digits[9]).pop()
            code_map["f"] = digits[1].difference(digits[2]).pop()
            blist = list(digits[4].difference(digits[3]))
            random.shuffle(blist)
            code_map["b"] = blist[0]
            clist = list(digits[8].difference(digits[6]))
            random.shuffle(clist)
            code_map["c"] = clist[0]
            code_map["g"] = digits[8].difference(set(code_map.values())).pop()

            for d,s in digits.items():
                if not s and d == 3:
                    digits[3] = set([code_map[char] for char in "acdfg"])

            val = ""
            valid = True
            for c in code:
                digit = next((d for d,s in digits.items() if s == c), None)
                if digit is None:
                    valid = False
                val += str(digit)
            if not valid:  # dirtiest practice i'm ashamed making use of
                continue
            return int(val)

    print(sum(map(decode, input)))

part_one()
part_two()
