test_data = '''
3   4
4   3
2   5
1   3
3   9
3   3
'''

def parse(input):
    left_list = []
    right_list = []
    pairs = input.split('\n')
    for pair in pairs:
        l,*_,r = pair.split(' ') 
        left_list.append(int(l.strip()))
        right_list.append(int(r.strip()))
    left_list.sort()
    right_list.sort()
    return (left_list,right_list)

def part1(left_list,right_list):
    sum_diff = 0
    for left,right in zip(left_list,right_list):
        sum_diff += abs(left-right)
    print(sum_diff)

def part2(left_list,right_list):
    a = []
    for id in left_list:
        a.append(id * right_list.count(id))
    print(sum(a))




with open('input_1.txt') as f :
    input = f.read()
    left_list, right_list = parse(input.strip())
    part1(left_list,right_list)
    part2(left_list,right_list)

