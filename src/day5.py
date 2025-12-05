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

ranges = sorted(ranges, key=lambda r: r[0])


part1 = 0

for ingredient in ingredients:
    for rangemin, rangemax in ranges:
        if ingredient <= rangemax and  ingredient >= rangemin:
            part1 += 1
            break
            

# print(ranges)
# print(ingredients)
print(part1)