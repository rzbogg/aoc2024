test_data = '''
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
'''



def extract_args(arguments):
    nums = arguments.split(",")
    if len(nums) != 2:
        return None
    try:
        x = int(nums[0])
        y = int(nums[1])
        return (x,y)
    except ValueError:
        return None 

# without regex bitch!!!
def extract_muls(data,ins_map):
    idx = -1
    while (idx := data.find('mul(',idx+1)) != -1:
        try:
            args = extract_args(data[idx+4:data.find(')',idx+4)])
            if args:
                ins_map[idx] = (args[0],args[1])
        except IndexError:
            return

def extract_dos(data,ins_map):
    idx = -1
    while (idx := data.find('do()',idx+1)) != -1:
        ins_map[idx] = 'do'

def extract_donts(data,ins_map):
    idx = -1
    while (idx := data.find('don\'t()',idx+1)) != -1:
        ins_map[idx] = 'dont'


def parse(data):
    instruction_map = {}
    instructions = []
    extract_muls(data,instruction_map)
    extract_dos(data,instruction_map)
    extract_donts(data,instruction_map)
    instruction_ids = [key for key in instruction_map.keys()]
    instruction_ids.sort()
    instructions = [instruction_map[id] for id in instruction_ids]
    return instructions



def part1(instructions):
    s = 0
    for ins in instructions:
        if ins == 'do' or ins =='dont':
            continue
        s += ins[0] * ins[1]
    return s

def part2(instructions):
    s = 0
    disable = False
    for ins in instructions:
        if ins == 'dont': 
            disable = True
            continue
        if ins == 'do': 
            disable = False
            continue
        if not disable and type(ins) == tuple:
            s += ins[0] * ins[1]
    return s


with open('input_3.txt') as f:
    data = f.read()
    instructions = parse(data.strip())
    print('part one = ', part1(instructions))
    print('part two = ', part2(instructions))

