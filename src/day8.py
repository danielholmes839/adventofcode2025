import itertools
from dataclasses import dataclass

@dataclass
class Circuit:
    distance: int
    points: list[int]

def calc_distance(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2


def merge(ci: int, cj: int, connection_distance: int, circuits: dict[int, Circuit], circuits_by_point: dict[int, int]):
    circuits[ci].points.extend(circuits[cj].points)
    circuits[ci].distance += circuits[cj].distance + connection_distance

    # update the point->circuit dict for future updates
    for point in circuits[cj].points:
        circuits_by_point[point] = ci
    del circuits[cj]

def part1(points):
    # adjacency list with only the shortest edge
    edges = []
    
    for i in range(len(points)):
        for j in range(i, len(points)):
            if i == j:
                continue
            
            distance = calc_distance(points[i], points[j])
            edges.append((i, j, distance))

    edges = sorted(edges, key=lambda edge: edge[2])
    
    c = 0
    circuits: dict[int, Circuit] = {} # circuit to list of points in a circuits
    circuits_by_point: dict[int, int] = {} # point -> circuit

    for (i, j, distance) in edges[:1000]:
        ci, cj = circuits_by_point.get(i), circuits_by_point.get(j)

        if ci == cj and ci is not None:
            # already in the same circuit
            continue

        if ci is None and cj is None:            
            # new circuit
            # connect i and j, inc distance of circuit
            # inc connections added
            circuits[c] = Circuit(
                distance=distance,
                points=[i, j]
            )
            circuits_by_point[i] = c
            circuits_by_point[j] = c
            c += 1

        elif ci is not None and cj is None:
            # i is connected to a circuit j is not
            circuits[ci].points.append(j)
            circuits[ci].distance += distance
            circuits_by_point[j] = ci

        
        elif cj is not None and ci is None:
            # j is connected to a circuit i is not
            circuits[cj].points.append(i)
            circuits[cj].distance += distance
            circuits_by_point[i] = cj
        
        else:
            # both i and j are in a circuit. merge the circuits
            merge(ci, cj, distance, circuits, circuits_by_point)
        

    largest_circuits = sorted(circuits.values(), key=lambda circuit: circuit.distance, reverse=True)

    part1 = 1
    for circuit in largest_circuits[:3]:
        part1 *= len(circuit.points)
    
    for circuit in largest_circuits[:10]:
        print(len(circuit.points), circuit.distance)
    return part1



def part2(points):
    # adjacency list with only the shortest edge
    edges = []
    
    for i in range(len(points)):
        for j in range(i, len(points)):
            if i == j:
                continue
            
            distance = calc_distance(points[i], points[j])
            edges.append((i, j, distance))

    edges = sorted(edges, key=lambda edge: edge[2])
    
    c = 0
    circuits: dict[int, Circuit] = {} # circuit to list of points in a circuits
    circuits_by_point: dict[int, int] = {} # point -> circuit

    for (i, j, distance) in edges:
        ci, cj = circuits_by_point.get(i), circuits_by_point.get(j)

        if ci == cj and ci is not None:
            # already in the same circuit
            continue

        if ci is None and cj is None:            
            # new circuit
            # connect i and j, inc distance of circuit
            # inc connections added
            circuits[c] = Circuit(
                distance=distance,
                points=[i, j]
            )
            circuits_by_point[i] = c
            circuits_by_point[j] = c
            c += 1

        elif ci is not None and cj is None:
            # i is connected to a circuit j is not
            circuits[ci].points.append(j)
            circuits[ci].distance += distance
            circuits_by_point[j] = ci

        
        elif cj is not None and ci is None:
            # j is connected to a circuit i is not
            circuits[cj].points.append(i)
            circuits[cj].distance += distance
            circuits_by_point[i] = cj
        
        else:
            # both i and j are in a circuit. merge the circuits
            merge(ci, cj, distance, circuits, circuits_by_point)
        
        if len(circuits) == 1 and len(list(circuits.values())[0].points) == len(points):
            print()
            return points[i][0] * points[j][0]

with open('data/day8.txt', 'r') as f:
    lines = f.readlines()


points = [tuple(int(d) for d in line.split(",")) for line in lines]
# print(points)
print(part1(points))
print(part2(points))
