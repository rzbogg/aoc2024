test_data = '''
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
'''

def in_range(letters,y,x):
    row_len = len(letters)
    col_len = len(letters[0])
    if y >= row_len or y < 0 or x >= col_len or x < 0:
        return False
    return True
    

def count_xmas_in_dir(letters,row,col,dir):
    word = 'X'
    y,x = dir
    for _ in range(3):
        if not in_range(letters,row+y,col+x):
            return 0
        next_letter = letters[row+y][col+x]
        word += next_letter
        y , x = y+dir[0], x+dir[1]
    if word == 'XMAS':
        return 1
    return 0

def count_xmas(letters,row,col):
    dirs = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
    count = 0
    for dir in dirs:
        count += count_xmas_in_dir(letters,row,col,dir)
    return count


def part1(letters):
    count = 0
    for row in range(len(letters)):
        for col in range(len(letters[row])):
            if letters[row][col] != 'X':
                continue
            count += count_xmas(letters,row,col)
    return count

def part2(letters):
    count = 0
    for row in range(1,len(letters)-1):
        for col in range(1,len(letters[row])-1):
            if letters[row][col] != 'A':
                continue
            s = {'M','S'}
            if {letters[row-1][col-1],letters[row+1][col+1]} == s and {letters[row+1][col-1], letters[row-1][col+1]} == s:
                count+=1
    return count

with open('input_4.txt') as f:
    data = f.read()
    letters = data.strip().split('\n')
    print('part one = ',part1(letters))
    print('part two = ',part2(letters))
