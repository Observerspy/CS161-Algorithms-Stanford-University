import numpy as np
from collections import defaultdict
import itertools
class MySet():
    def __init__(self, par, rank):
        self.parent = par
        self.rank = rank


def find(a, i):
    if a[i].parent != i:
        a[i].parent = find(a, a[i].parent)
    return a[i].parent


def union(a, x, y):
    xroot = find(a, x)
    yroot = find(a, y)
    if a[xroot].rank < a[yroot].rank :
        a[xroot].parent = yroot
    elif a[xroot].rank > a[yroot].rank :
        a[yroot].parent = xroot
    else:
        a[yroot].parent = xroot
        a[xroot].rank += 1


if __name__ == '__main__':
    with open('cluster_big.txt', 'r') as f:
        mylist = f.readlines()
    a = [int(str.split('\n')[0].replace(" ",""), 2) for i, str in enumerate(mylist[1:])]
    d = {}
    for i, l in enumerate(a):
        if l in d:
            d[l].append(i)
        else:
            d[l] = [i]
    c = []
    for bits in itertools.combinations(range(24), 1):
        zeros = ['0'] * 24
        for bit in bits:
            zeros[bit] = '1'
        c.append(int(''.join(zeros), 2))
    for bits in itertools.combinations(range(24), 2):
        zeros = ['0'] * 24
        for bit in bits:
            zeros[bit] = '1'
        c.append(int(''.join(zeros), 2))


    s = []
    for i in range(200000):
        o = MySet(i, 0)
        s.append(o)

    for v in range(len(a)):
        set1 = find(s, v)
        for idx in d[a[v]]:
            if idx != v:
                set2 = find(s, idx)
                union(s, set1, set2)

        for ner in c:
            if a[v] ^ ner in d:
                for idx in d[a[v] ^ ner]:
                    set2 = find(s, idx)
                    union(s, set1, set2)

    # print(set([find(s, i) for i in range(200000)]))
    print(len(set([find(s, i) for i in range(200000)]))) #6118

