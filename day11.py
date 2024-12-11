from sys import argv 

test_data = '125 17'


def blink(stone,blinks,cache):
    if blinks == 0:
        return 1

    if (stone,blinks) in cache:
        return cache[(stone,blinks)]
    if stone == 0:
        size = blink(1,blinks-1,cache)
    elif (digits:=len(str(stone))) % 2 == 0:
        left = stone // 10 ** (digits//2)
        right = stone % 10 ** (digits//2)
        size = blink(left,blinks-1, cache) + blink(right,blinks-1,cache)
    else:
        size = blink(stone*2024,blinks-1,cache)
    if (stone,blinks) not in cache:
        cache[(stone,blinks)] = size
    return size

def part1(stones):
    cache = {}
    return sum([blink(stone,25,cache) for stone in stones])


def part2(stones):
    cache = {}
    return sum([blink(stone,75,cache) for stone in stones])

if __name__ == '__main__':
    data = None
    if len(argv) == 1:
        data = test_data
    else:
        file_name = argv.pop()
        with open(file_name) as f:
            data = f.read()
    numbers = list(map(int,data.strip().split(' ')))
    print('part one = ', part1(numbers))
    print('part two = ', part2(numbers))

