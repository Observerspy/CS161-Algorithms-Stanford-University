import numpy as np
import random
from tqdm import trange
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
    with open('week4.input', 'r') as f:
        mylist = f.readlines()
    a = [np.array(str.split('\n')[0].split('\t'), dtype=int) for str in mylist]
    a = np.array(a)

    E = []
    for l in a:
        E.extend( [(l[0], l[i]) if l[0] < l[i] else (l[i], l[0]) for i in range(1, len(l)) ] )
    E_set = list(set(E))
    mincut = len(E_set)
    for _ in trange(100000):
        v_num = a.shape[0]
        s = []
        for i in range(v_num):
            o = MySet(i, 0)
            s.append(o)

        while v_num > 2:
            randIndex = random.randint(0, len(E_set)-1)
            set1 = find(s, E_set[randIndex][0]-1)
            set2 = find(s, E_set[randIndex][1]-1)

            if set1 == set2:
                continue
            else:
                v_num -= 1
                union(s, set1, set2)

        count = 0
        for i in range(len(E_set)):
            set1 = find(s, E_set[i][0]-1)
            set2 = find(s, E_set[i][1]-1)
            if set1 != set2:
                count += 1

        if count < mincut:
            mincut = count
            print(mincut)
    print(mincut)