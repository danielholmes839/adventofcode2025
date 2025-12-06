with open('data/day6.txt', 'r') as f:
    lines = f.read().splitlines()


ops = list(filter(lambda op: op != '', lines[-1].split(" ")))

values = []
for op in ops:
    if op == '*':
        values.append(1)
    else:
        values.append(0)

for line in lines[:-1]:
    nums = [int(num) for num in line.split(" ") if num.isdecimal()]
    for i, num, op in zip(range(len(ops)), nums, ops):
        if op == '*':
            values[i] *= num
        else:
            values[i] += num

print(sum(values))
