import numpy as np
from collections import defaultdict
import sys
from tqdm import trange

if __name__ == '__main__':
    with open('nn.txt', 'r') as f:
        mylist = f.readlines()
    l = []
    for lines in mylist[1:]:
        lines = lines.split(' ')
        l.append([float(lines[0]), float(lines[1]), float(lines[2])])
    city_num = 33708
    v = {i for i in range(1, city_num)}
    # visit = defaultdict(lambda :False)
    # visit[0] = True
    path = [0]
    sumd = 0
    for i in trange(city_num-1):
        mind = sys.maxsize
        for _,j in enumerate(v):
        # for j in range(city_num):
        # if not visit[j]:
            x_diff = (l[path[i]][1] - l[j][1]) ** 2
            if x_diff < mind:
                dist = (l[path[i]][1] - l[j][1]) ** 2 + (l[path[i]][2] - l[j][2]) ** 2#np.sum((l[path[i - 1]] - l[j]) ** 2)
                if dist < mind:
                    mind = dist
                    node = j
        path.append(node)
        sumd += np.sqrt(mind)
        # visit[node] = True
        v.remove(node)
    print(path)
    print(sumd + np.sqrt((l[path[-1]][1] - l[0][1]) ** 2 + (l[path[-1]][2] - l[0][2]) ** 2))