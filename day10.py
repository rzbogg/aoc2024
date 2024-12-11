from sys import argv

test_data = '''
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
'''


def find_trailheads(grid):
    result = []
    for y,row in enumerate(grid):
        for x,cell in enumerate(row):
            if cell == 0:
                result.append((y,x))
    return result



def in_range(pos,grid):
    row_size = len(grid) 
    col_size = len(grid[0])
    y = pos[0]
    x = pos[1]
    if y < 0 or y >= row_size or x < 0 or x >= col_size:
        return False    
    return True


def rating(grid,pos):
    dirs = [(1,0),(-1,0),(0,-1),(0,1)]
    s = 0
    def walk(pos):
        nonlocal s
        cell = grid[pos[0]][pos[1]]
        if cell == 9:
            s +=1
            return
        for dir in dirs:
            next_pos = (pos[0]+dir[0],pos[1]+dir[1])
            if not in_range(next_pos,grid): continue
            next_cell = grid[next_pos[0]][next_pos[1]]
            if next_cell == cell + 1 :
                walk(next_pos)
    walk(pos)
    return s


def score(grid,pos):
    visited_nines = set()
    dirs = [(1,0),(-1,0),(0,-1),(0,1)]
    s = 0
    def walk(pos):
        nonlocal s
        cell = grid[pos[0]][pos[1]]
        if cell == 9:
            visited_nines.add(pos)
            s +=1
            return
        for dir in dirs:
            next_pos = (pos[0]+dir[0],pos[1]+dir[1])
            if not in_range(next_pos,grid): continue
            next_cell = grid[next_pos[0]][next_pos[1]]
            if next_cell == cell + 1 and next_pos not in visited_nines:
                walk(next_pos)
    walk(pos)
    return s


def part1(grid):
    trailheads = find_trailheads(grid)
    assert trailheads
    s = 0
    for pos in trailheads:
        s += score(grid,pos)
    return s


def part2(grid):
    trailheads = find_trailheads(grid)
    assert trailheads
    s = 0
    for pos in trailheads:
        s += rating(grid,pos)
    return s




if __name__ == '__main__':
    data = None
    if len(argv) == 1:
        data = test_data
    else:
        file_name = argv.pop()
        with open(file_name) as f:
            data = f.read()
    grid = [list(map(int,list(row))) for row in data.strip().split('\n')]
    print('part one = ', part1(grid))
    print('part two = ', part2(grid))

