



class Solver:
    def __init__(self):
        self.cache = {}
    
    def solve(self, line_str, line_num, n):
        if len(line_str) == n:
            return int(line_str)
        
        if len(line_str) < n:
            return -1
        
        if (line_str, n) in self.cache:
            return self.cache[(line_str, n)]
        
        if n == 1:
            return max(line_num)
        
        include = self.solve(line_str[1:], line_num[1:], n-1) + (line_num[0] * (10 ** (n-1)))
        exclude = self.solve(line_str[1:], line_num[1:], n)

        # print(line_str,  n, include, exclude)


        best = max(include, exclude)
        self.cache[(line_str, n)] = best
        return best


with open('data/day3.txt', 'r') as f:
    lines = f.read().splitlines()

solver = Solver()

part2 = 0
for i, line in enumerate(lines):
    part2 += solver.solve(line, [int(n) for n in list(line)], 12)
    # print(solver.cache)

# part2 += solver.solve("11112", [1, 1, 1, 1, 2], 2)

print(part2)