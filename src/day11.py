with open('data/day11.txt', 'r') as f:
    lines = f.readlines()

graph: dict[str, list[str]] = {}

for line in lines:
    node = line[:3]
    edges = line[5:].strip().split(" ")
    graph[node] = edges

graph['out'] = []


def part1(graph: dict[str, list[str]], start: str, end: str):
    memo = {}

    def count(node: str, destination: str):
        if node == destination:
            return 1
        
        if node in memo:
            return memo[node]
        
        paths = sum(count(neighbor, end) for neighbor in graph[node])
        memo[node] = paths
        return paths
    
    return count(start, end)


def part2(graph: dict[str, list[str]]):
    # path 1
    svr_dac = part1(graph, 'svr', 'dac')
    dac_fft = part1(graph, 'dac', 'fft')
    fft_out = part1(graph, 'dac', 'out')
    path1 = svr_dac * dac_fft * fft_out

    # path 2
    svr_fft = part1(graph, 'svr', 'fft')
    fft_dac = part1(graph, 'fft', 'dac') 
    dac_out = part1(graph, 'dac', 'out')
    path2 = svr_fft * fft_dac * dac_out

    print(path1, path2) # one path should be 0 otherwise there's a cycle.

    return path1 + path2



count = part1(graph, 'you', 'out')
print(count)

count = part2(graph)
print(count)