from dataclasses import dataclass
test_data = '2333133121414131402'


@dataclass
class Block:
    type: str
    start: int
    size : int
    id: int|None = None


def parse_disk(disk_map):
    file_blocks = []
    free_blocks = []
    id = 0
    start = 0
    for i,n in enumerate(disk_map):
        if i % 2 == 0:
            file_blocks.append(Block('file',start,int(n),id))
            id+=1
        else:
            free_blocks.append(Block('space',start,int(n)))
        start+=int(n)
    return file_blocks,free_blocks

def block_checksum(block):
    cs = 0
    for i in range(block.start,block.start+block.size):
        cs += i * block.id
    return cs
        


def checksum(file_blocks):
    cs = 0
    for block in file_blocks:
        cs += block_checksum(block)
    return cs


def part2(file_blocks,free_blocks):
    for i in range(len(free_blocks),-1,-1):
        last_file_block = file_blocks[i]
        free_block = None
        for gap in free_blocks:
            if gap.start > last_file_block.start:
                break
            if gap.size >= last_file_block.size:
                free_block = gap
                break
        if not free_block: continue
        last_file_block.start = free_block.start
        free_block.start += last_file_block.size
        free_block.size -= last_file_block.size
    return checksum(file_blocks)




with open('input_9.txt') as f:
    data = f.read()
    file_blocks,free_blocks = parse_disk(data.strip())
    print('part one = ',part2(file_blocks,free_blocks))
