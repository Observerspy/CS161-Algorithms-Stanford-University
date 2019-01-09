import numpy as np
import sys
INF = sys.maxsize

if __name__ == '__main__':
    with open('test.txt', 'r') as f:
        mylist = f.readlines()
    a = [np.array(str.split('\n')[0].split(' '), dtype=int) for str in mylist[1:]]
    E = {}
    for l in a:
        E[str(l[0])+'-'+str(l[1])] = l[2]
    vnum = 5
    D = np.zeros((vnum, vnum))
    for i in range(vnum):
        for j in range(vnum):
            D[i][j] = E.get(str(i+1)+'-'+str(j+1), INF)

    for k in range(vnum):
        for i in range(vnum):
            for j in range(vnum):
                if (D[i, j] > D[i, k] + D[k, j]):
                    D[i, j] = D[i, k] + D[k, j]

    for i in range(vnum):
        if D[i][i] < 0:
            print('NULL')
            break
    print(D, np.min(D))
