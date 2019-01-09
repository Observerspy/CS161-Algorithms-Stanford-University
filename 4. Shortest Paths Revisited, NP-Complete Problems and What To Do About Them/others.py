import sys

from math import sqrt
from itertools import combinations


def construct(file_path):
    vertices = []

    with open(file_path) as file:
        file.readline()

        for line in file:
            item = line.split()
            vertices.append((float(item[0]), float(item[1])))

    return vertices


def tsp(start, end, points):
    n = len(points) + 1
    d = generate_distances([start] + points + [end])

    A = {}
    for i in range(1, n):
        A[encode([0, i], n), i] = d[0][i]

    for m in range(2, n):
        B = {}
        for S in [set(subset) | {0} for subset in combinations(range(1, n), m)]:
            for j in S - {0}:
                C = [A[encode(S - {j}, n), k] + d[k][j] for k in S if k != 0 and k != j]
                B[encode(S, n), j] = min(C)
        A = B

    return min([A[a] + d[a[1]][n] for a in A])


def encode(subset, n):
    zeros = ['0'] * n

    for element in subset:
        zeros[element] = '1'

    return int(''.join(reversed(zeros)), 2)

def decode(number):
    subset = []

    for index, bit in enumerate(reversed(bin(number)[2:])):
        if bit == '1':
            subset.append(index)

    return set(subset)


def generate_subsets(n, r):
    result = []

    for bits in combinations(range(n), r):
        result.append(encode(bits, n))

    return result

def generate_grouped_subsets(n):
    subsets = {}

    for r in range(n + 1):
        subsets[r] = generate_subsets(n, r)

    return subsets


def distance(x, y):
    return sqrt(((x[0] - y[0]) ** 2) + ((x[1] - y[1]) ** 2))

def generate_distances(points):
    return [[distance(x, y) for y in points] for x in points]


def main(argv):
    vertices  = construct('tsp.txt')

    d = tsp(vertices[0], vertices[0], vertices[1:])

    print ('Shortest Distance: ', d)


if __name__ == "__main__":
    main('tsp.txt')