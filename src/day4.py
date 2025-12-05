offsets = [(0, 1), (-1, -1), (-1, 1), (1, 1), (1, -1), (-1, 0), (1, 0), (0, -1)]

with open('data/day4.txt', 'r') as f:
    lines = f.read().splitlines()


part1 = 0

for r, line in enumerate(lines):
    for c, val in enumerate(line):
        if val != "@":
            # print(".", end="")
            continue

        adjacent_count = 0

        for dr, dc in offsets:
            nr, nc = r + dr, c + dc
            if nr < 0 or nc < 0 or nr >= len(lines) or nc >= len(line):
                continue

            adjacent = lines[nr][nc]

            if adjacent == "@":
                # print("@")
                adjacent_count += 1

        if adjacent_count < 4:
            part1 += 1
            
            # print(adjacent_count, end="")
            # print("x", end="")
        # else:
            
            # print(adjacent_count, end="")
            # print("@", end="")

print(part1)
