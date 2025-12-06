def part1(data: str) -> int:
    lines = data.splitlines()
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

    return sum(values)


def part2(data: str):
    lines = data.splitlines()
    ops = list(filter(lambda op: op != '', lines[-1].split(" ")))

    values = []
    for op in ops:
        if op == '*':
            values.append(1)
        else:
            values.append(0)
    

    data = data.replace("\n", "")

    part2 = 0


    i = 0
    acc = 0
    if ops[i] == '*':
        acc = 1
    else:
        acc = 0

    for col in range(len(lines[0])):
        num = data[col:(len(lines)-1)*len(lines[0]):len(lines[0])].strip()
        if num == '':
            part2 += acc
            i += 1
            if i == len(ops):
                break

            if ops[i] == '*':
                acc = 1
            else:
                acc = 0

            continue
        
        num = int(num)
        if ops[i] == '*':
            acc *= num
        else:
            acc += num

    part2 += acc

    return part2

with open('data/day6.txt', 'r') as f:
    data = f.read()

print(part1(data))
print(part2(data))


