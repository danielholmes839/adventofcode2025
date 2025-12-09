with open('data/day9.txt', 'r') as f:
    tiles = [tuple(int(d) for d in line.split(",")) for line in  f.readlines()]

print(tiles)

largest_area = 0

for i, ti in enumerate(tiles):
    for tj in tiles[i+2:]:
        length = abs(ti[0] - tj[0])+1
        width = abs(ti[1] - tj[1])+1
        largest_area = max(largest_area, length * width)

print(largest_area)