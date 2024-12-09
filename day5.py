from collections import defaultdict


test_data = '''
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
'''





def parse(input):
    rule_part, update_part = input.split('\n\n')
    rules = defaultdict(list)
    for x,y in [pair.split('|') for pair in rule_part.split('\n')]:
        x,y = int(x),int(y)
        rules[y].append(x)
    updates = []
    for update in update_part.split('\n'):
        updates.append([int(x) for x in update.split(',')])
    return (rules,updates)

def in_order(update,rules):
    for i,page in enumerate(update):
        for j in range(i+1,len(update)):
            if update[j] in rules[page]:
                return False, (i,j)
    return True, None


def part1(updates,rules):
    c = 0
    for update in updates:
        ordered, _ = in_order(update,rules)
        if ordered:
            c += update[int(len(update)/2)]
    return c

def part2(updates,rules):
    c = 0
    for update in updates:
        ordered, xy = in_order(update,rules)
        oo = ordered
        while not ordered:
            assert xy is not None
            x,y = xy
            temp = update[x]
            update[x] = update[y]
            update[y] = temp
            ordered, xy = in_order(update,rules)
        if not oo:
            c += update[int(len(update)/2)]

    return c


with open('input_5.txt') as f:
    data = f.read()
    rules, updates = parse(data.strip())
    print('part one=',part1(updates,rules))
    print('part two=',part2(updates,rules))
