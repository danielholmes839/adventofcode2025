
def split(lines: str, hit: set, i: int, j: int):
    if i == len(lines):
        return 0
    
    # avoid already explored splitters
    if (i, j) in hit:
        return 0

    if lines[i][j] == '.':
        # continue moving down
        split(lines, hit, i+1, j)
    
    else:
        hit.add((i, j))
        split(lines, hit, i, j+1)
        split(lines, hit, i, j-1)


with open('data/day7.txt', 'r') as f:
    lines = f.readlines()

hit = set()

j = lines[0].find("S")
split(lines, hit, 1, j)
print(len(hit))
