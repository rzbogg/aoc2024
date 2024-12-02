test_data = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''


def parse(input):
    reports = [ list(map(int,report.strip().split(' '))) for report in input.split('\n')]
    return reports

def is_safe(report):
    diffs = [report[i+1] - report[i] for i in range(0,len(report)-1)]
    inc = all(diff >= 0 for diff in diffs)
    dec = all(diff <= 0 for diff in diffs)
    in_range = all( abs(diff) >= 1 and abs(diff) <= 3 for diff in diffs)
    if in_range and (inc or dec):
        return True
    return False


def part1(reports):
    safe_count = 0
    for report in reports:
        if is_safe(report): safe_count+=1
    return safe_count

def part2(reports):
    safe_count = 0
    for report in reports:
        if is_safe(report): safe_count+=1
        else:
            for i in range(len(report)):
                new_report = report[:i] + report[i+1:]
                if is_safe(new_report):
                    safe_count+=1
                    break
    return safe_count


with open('input_2.txt') as f:
    input = f.read()
    reports = parse(input.strip())
    print('part one =',part1(reports))
    print('part one =',part2(reports))
