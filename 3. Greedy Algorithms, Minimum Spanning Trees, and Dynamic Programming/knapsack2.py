import numpy as np
import sys
d = {}
def solve(a, w):
    r = 0
    if len(a) == 0:
        return 0
    val1 = d.get((len(a[:-1]), w))
    if val1 is None:
        val1 = solve(a[:-1], w)
        d[(len(a[:-1]), w)] = val1
    val2 = 0
    if w > a[-1][1]:
        val2 = d.get((len(a[:-1]), w - a[-1][1]))
        if val2 is None:
            val2 = solve(a[:-1], w - a[-1][1])
            d[(len(a[:-1]), w - a[-1][1])] = val2
        val2 += a[-1][0]
    r = max(val1, val2)
    return r

if __name__ == '__main__':
    sys.setrecursionlimit(2000000 + 200)
    with open('knapsack_big.txt', 'r') as f:
        mylist = f.readlines()
    l = [np.array(i.split('\n')[0].split(' '), dtype=int) for i in mylist[1:]]
    print(solve(l, 2000000))
    # a = np.zeros((2000000+1))
    # for i in range(1, 2000):
    #     for j in range(2000000, l[i][1]-1, -1):
    #         if j >= l[i][1]:
    #             a[j] = max(a[j], a[j-l[i][1]]+l[i][0])
    #         else:
    #             a[j] = a[j]
    # print(a[-1])#4243395