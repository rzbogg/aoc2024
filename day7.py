test_data = '''
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
'''

def parse_equations(data):
    result = []
    for line in data:
        value, numbers = line.split(':')
        value = int(value)
        numbers = list(map(int,numbers.strip().split()))
        result.append((value,numbers))
    return result

def is_correct(equation,ops):
    results = []
    numbers = equation[1]
    test_value = equation[0]
    possibles = [numbers.pop(0)]
    while numbers:
        current = numbers.pop(0)
        next_pos = []
        for p in possibles:
            for op in ops:
                match op:
                    case '*' : next_pos.append(p*current)
                    case '+' : next_pos.append(p+current)
                    case '||' : next_pos.append(int(str(p)+str(current)))
        possibles = [v for v in next_pos if v <= test_value ]
    if test_value in possibles:
        return True
    return False 

def part1(equations):
    ops = ['*','+']
    result = 0
    for equation in equations:
        if is_correct(equation,ops):
            result += equation[0]
    return result

def part2(equations):
    ops = ['*','+','||']
    equations = parse_equations(data)
    result = 0
    for equation in equations:
        if is_correct(equation,ops):
            result += equation[0]
    return result


with open('input_7.txt') as f :
    data = f.read()
    data = data.strip().split('\n')
    equations = parse_equations(data)
    print('part one = ',part1(equations))
    print('part two = ',part2(equations))

