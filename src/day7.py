
def part1(lines: str, hit: set, i: int, j: int):
    if i == len(lines):
        return 0
    
    # avoid already explored splitters
    if (i, j) in hit:
        return 0

    if lines[i][j] == '.':
        # continue moving down
        part1(lines, hit, i+1, j)
    
    else:
        hit.add((i, j))
        part1(lines, hit, i, j+1)
        part1(lines, hit, i, j-1)


def part2(lines: str, cache: dict, i: int, j: int):
    if i == len(lines):
        return 1 # we complete a path
    
    if (i, j) in cache:
        return cache[(i, j)]

    if lines[i][j] == '.':
        # continue moving down
        return part2(lines, cache, i+1, j)
    
    else:
        # update the number of timelines following this splitter
        timelines = part2(lines, cache, i, j+1) + part2(lines, cache, i, j-1)
        cache[(i,j)] = timelines
        return timelines

with open('data/day7.txt', 'r') as f:
    lines = f.readlines()

# part 1
hit = set()
j = lines[0].find("S")
part1(lines, hit, 1, j)
print(len(hit))

# part 2
print(part2(lines, dict(), 1, j))
