test_data = '''
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
'''


def get_gaurd_pos(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '^':
                return (i,j)



def walk(grid,pos=None,i=None):
    if not pos:
        pos = get_gaurd_pos(grid)
    if not i:
        i = 0
    assert pos != None
    dirs = [(-1,0),(0,1),(1,0),(0,-1)]
    path = set()
    path.add(pos)
    visited_blocks = {}
    while True:
            next_pos = (pos[0]+dirs[i][0], pos[1]+dirs[i][1])
            if next_pos[0] < 0 or next_pos[0] >= len(grid) or next_pos[1] < 0 or next_pos[1] >= len(grid[1]):
                return path,False,visited_blocks
            next_block = grid[next_pos[0]][next_pos[1]]
            if next_block == '#':
                i = (i + 1) % len(dirs)
            else:
                if next_pos not in visited_blocks:
                    visited_blocks[next_pos] = (i,pos)
                elif visited_blocks[next_pos] == (i,pos):
                    return None,True,None
                path.add(next_pos)
                pos = next_pos




def part1(grid):
    path,_,_ = walk(grid)
    if not path : return 0
    return len(path)

def part2(grid):
    _grid = [list(row) for row in grid]
    pos = get_gaurd_pos(_grid)
    assert pos != None
    path,stuck,visited_blocks = walk(_grid)
    assert path != None and visited_blocks != None
    path.remove(pos)
    loops = 0
    for row,col in path:
        _grid[row][col] = '#'
        # check for loop 
        i,pos = visited_blocks[(row,col)] 
        _,stuck,_ = walk(_grid,pos,i)
        if stuck: loops += 1
        _grid[row][col] = '.'
    return loops


with open('input_6.txt') as f:
    data = f.read()
    grid = data.strip().split('\n')
    print('part one = ',part1(grid))
    print('part two = ', part2(grid))
