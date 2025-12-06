with open('data/day5.txt', 'r') as f:
    lines = f.read().splitlines()

ranges = []
ingredients = []

for line in lines:
    if line == "":
        continue
    
    ingredient_or_range = tuple(int(num) for num in line.split("-"))
    if len(ingredient_or_range) == 2:
        ranges.append(ingredient_or_range)
    
    else:
        ingredients.append(ingredient_or_range[0])




part1 = 0

for ingredient in ingredients:
    for rangemin, rangemax in ranges:
        if ingredient <= rangemax and  ingredient >= rangemin:
            part1 += 1
            break
 

def merge_ranges(ranges):
    grouped_ranges = []

    for (rmin, rmax) in ranges:
        grouped = False
        for i, (grmin, grmax) in enumerate(grouped_ranges):
            if (rmin >= grmin and rmin <= grmax) or (rmax >= grmin and rmax <= grmax):
                grouped_ranges[i] = (min(rmin, grmin), max(rmax, grmax))
                grouped = True
                break
        
        if not grouped:
            grouped_ranges.append((rmin, rmax))
    
    return grouped_ranges

i = 0
ranges = sorted(ranges, key=lambda r: r[0])
ranges = merge_ranges(ranges)
part2 = 0

for (rmin, rmax) in ranges:
    part2 += (rmax - rmin)+1

print(part2)


# print(ranges)
# print(ingredients)
# print(part1)