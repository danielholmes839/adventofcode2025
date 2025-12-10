def parse_input(line: str):
    sections = line.split(" ")
    
    configuration = []
    for c in sections[0][1:-1]:
        if c == '.':
            configuration.append(0)
        else:
            configuration.append(1)
    
    configuration = tuple(configuration)

    buttons = []
    for section in sections[1:-1]:
        button = []
        for n in section[1:-1].split(","):
            button.append(int(n))
        buttons.append(tuple(button))
    
    return configuration, buttons
        
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
                new_configuration[i] = new_configuration[i] ^ 1 
            new_configuration = tuple(new_configuration)
            queue.append((depth + 1, new_configuration))
        

    return depth



    
with open('data/day10.txt', 'r') as f:
    lines = f.readlines()

total_part1 = 0

for line in lines:
    configuration, buttons = parse_input(line)
    total_part1 += part1(configuration, buttons)

print(total_part1)