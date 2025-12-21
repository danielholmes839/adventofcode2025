import heapq

def parse_input(line: str):
    sections = line.strip().split(" ")
    
    configuration = []
    for c in sections[0][1:-1]:
        if c == '.':
            configuration.append(0)
        else:
            configuration.append(1)
    
    configuration = tuple(configuration)

    buttons = []
    for section in sections[1:]:
        button = []
        for n in section[1:-1].split(","):
            button.append(int(n))
        buttons.append(tuple(button))
    
    return configuration, buttons[:-1], buttons[-1]
        
def part1(final_configuration: tuple[int], buttons: list[tuple[int]]):
    depth = 0

    seen = set()
    initial_configuration = tuple([0] * len(final_configuration))

    queue = [(0, initial_configuration)]
    while len(queue) > 0:
        depth, configuration = queue.pop(0)

        if configuration == final_configuration:
            return depth

        if configuration in seen:
            continue
        
        seen.add(configuration)

        for button in buttons:
            new_configuration = list(configuration)
            for i in button:
                new_configuration[i] ^= 1 
            new_configuration = tuple(new_configuration)
            queue.append((depth + 1, new_configuration))
        

    return depth


def part2(final_configuration: tuple[int], buttons: list[tuple[int]]):
    depth = 0

    seen = set()
    initial_configuration = tuple([0] * len(final_configuration))

    queue = []
    
    heapq.heappush(queue, (0, (0, initial_configuration)))
    explorations = 0

    while len(queue) > 0:
        explorations += 1
        
        distance, (depth, configuration) = heapq.heappop(queue)
        print(distance, depth, configuration)
        # print(depth, configuration)

        if configuration in seen:
            continue
        
        if configuration == final_configuration:
            return depth, explorations

        
        seen.add(configuration)


        for button in buttons:
            new_configuration = list(configuration)
            distance = 0
            valid = True
            for i in button:
                new_configuration[i] += 1
                if new_configuration[i] > final_configuration[i]:
                    valid = False
                    break
            
            if not valid:
                continue
            
            for i in range(len(configuration)):
                distance += final_configuration[i] - new_configuration[i]

            new_configuration = tuple(new_configuration)

            heapq.heappush(queue, (distance, (depth + 1, new_configuration)))
        
    
with open('data/day10.txt', 'r') as f:
    lines = f.readlines()

total_part1 = 0
total_part2 = 0

for i, line in enumerate(lines):
    final_configuration_part1, buttons, final_configuration_part2 = parse_input(line)
    total_part1 += part1(final_configuration_part1, buttons)
    inc, explorations = part2(final_configuration_part2, buttons)

    total_part2 += inc
    print(explorations)
    break

    # break

print(total_part1, total_part2)