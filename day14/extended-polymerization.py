with open("day14/input") as f:
    input = list(map(str.strip, f.readlines()))

template = input[0]
rules = dict(rule.split(" -> ") for rule in input[2:])
rule_map = {rule:[rule[0] + rules[rule], rules[rule] + rule[1]] for rule in rules}
appearances = {key:template.count(key) for key in set("".join(list(rules.keys())))}
template_pairs = ["".join(_) for _ in zip(template, template[1:])]
freqs = {rule:template_pairs.count(rule) for rule in rules}

for _ in range(40):
    if _ == 10:
        print(max(appearances.values()) - min(appearances.values()))
    new_freqs = {rule:0 for rule in rules}
    for rule, freq in freqs.items():
        if freq > 0:
            appearances[rule_map[rule][0][1]] += freq
            r1, r2 = rule_map[rule]
            new_freqs[r1] += freq
            new_freqs[r2] += freq
    freqs = new_freqs
print(max(appearances.values()) - min(appearances.values()))
