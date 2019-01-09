import numpy as np
import sys
import threading
# 获取翻转所有边的图
def tr(G):
    # 初始化翻转边的图GT
    GT = dict()
    for u in G.keys():
        GT[u] = GT.get(u, set())
    # 翻转边
    for u in G.keys():
        for v in G[u]:
            GT[v].add(u)
    return GT


# 获取按节点遍历完成时间递减排序的顺序
def topoSort(G):
    res = []
    S = set()

    # dfs遍历图
    def dfs(G, u):
        if u in S:
            return
        S.add(u)
        for v in G[u]:
            if v in S:
                continue
            dfs(G, v)
        res.append(u)

    # 检查是否有遗漏的节点
    for u in G.keys():
        dfs(G, u)
    # 返回拓扑排序后的节点列表
    res.reverse()
    return res


# 通过给定的起始节点，获取单个连通量
def walk(G, s, S=None):
    if S is None:
        s = set()
    Q = []
    P = dict()
    Q.append(s)
    P[s] = None
    while Q:
        u = Q.pop()
        for v in G[u]:
            if v in P.keys() or v in S:
                continue
            Q.append(v)
            P[v] = P.get(v, u)
    # 返回强连通图
    return P

def main():
    with open('2sat6.txt', 'r') as f:
        mylist = f.readlines()
    n = 1000000
    G = {}
    for u in range(1, n+1):
        G[u] = G.get(u, set())
    for u in range(-n, 0):
        G[u] = G.get(u, set())
    for s in mylist[1:]:
        line = s.split('\n')[0].split(' ')[:2]
        G[-int(line[0])].add(int(line[1]))
        G[-int(line[1])].add(int(line[0]))

    # 记录强连通分量的节点
    seen = set()
    # 储存强强连通分量
    scc = []
    GT = tr(G)
    for u in topoSort(G):
        if u in seen:
            continue
        C = walk(GT, u, seen)
        seen.update(C)
        if len(C) > 1:
            scc.append(sorted(list(C.keys())))
    flag = 0
    for l in scc:
        for v in l:
            if -v in l:
                flag = 1
                print('Unsatisfiable')
                break
    if flag ==0:
        print('satisfiable')#101100


if __name__ == '__main__':
    threading.stack_size(67108864)
    sys.setrecursionlimit(2 ** 20)
    thread = threading.Thread(target=main)
    thread.start()