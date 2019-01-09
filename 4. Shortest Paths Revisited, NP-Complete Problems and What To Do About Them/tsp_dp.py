import numpy as np
from collections import defaultdict
import gc
from tqdm import trange
import sys
def TSP(s,init):
    if dp[(s,init)] !=-1 :
        return dp[(s,init)]
    if s==(1<<(city_num)):
        return dist[0][init]
    sumpath=1000000000
    for i in range(city_num):
        if s&(1<<i):
            m=TSP(s&(~(1<<i)),i)+dist[i][init]
            if m<sumpath:
                sumpath=m
                # path[s][init]=i
    dp[(s,init)]=sumpath
    return dp[(s,init)]

curIndexOfMap = 0
curIndexMap = {}
def getCurIndex(key):
    global curIndexOfMap,curIndexMap
    if key not in curIndexMap:
        curIndexMap[key] = curIndexOfMap
        curIndexOfMap += 1
    return curIndexMap[key]


def TSP3():
    global curIndexOfMap,curIndexMap
    curDp = {}
    curNum = set()
    for i in range(city_num-1):
        key = 1<<i
        index = getCurIndex(key)
        curDp[(index,i)] = dist[0][i+1] #0到i+1
        curNum.add(key)
    for i in trange(2, city_num):
        prevDp = curDp
        prevNum = curNum
        prevIndexMap = curIndexMap
        print(sum([sys.getsizeof(prevDp), sys.getsizeof(prevNum), sys.getsizeof(prevIndexMap)])/1024**2)
        curDp = {}
        curNum = set()
        curIndexMap = {}
        curIndexOfMap = 0
        #从起点出发经过key回到k
        for _, key in enumerate(prevNum):#key是子集
            for k in range(city_num - 1):#回到k
                if key & (1 << k) != 0:#k不应在key中
                    continue
                curKey = key | (1 << k)#去curKey集合，由子集key和出发点k构成
                for m in range(city_num - 1):#去子集key中的点m
                    if key & (1 << m) == 0:#m应在key中
                        continue
                    index = prevIndexMap[key]
                    curIndex = getCurIndex(curKey)
                    preval = curDp.get((curIndex,k), 0)
                    val = prevDp[(index,m)] + dist[m+1][k+1]#经m回到k
                    if preval == 0 or preval > val:
                        curDp[(curIndex,k)] = val
                curNum.add(curKey)

    key = (1<<(city_num-1))-1
    index = getCurIndex(key)
    mind = 999999999
    for i in range(city_num - 1):
        mind = min(mind, curDp[(index,i)] + dist[i + 1][0])
    return mind


def TSP2():
    for i in range(city_num):
        dp[(i, 0)] = dist[i][0]
    for j in range(1, 1<<(city_num -1)):
        for i in range(city_num):
            dp[(i, j)] = 9999999
            if i > 0 and ((j >> (i -1)) & 1 ) == 1:
                continue
            for k in range(1, city_num):
                if ((j >> (k - 1)) & 1) == 0:
                    continue
                val = dist[i][k] + dp[(k, j^(1 << (k-1)))]
                if dp[(i, j)] > val:
                    dp[(i, j)] = val
    return dp[(0, (1<<(city_num-1))-1)]


if __name__ == '__main__':
    with open('tsp.txt', 'r') as f:
        mylist = f.readlines()
    l = [np.array(i.split('\n')[0].split(' '), dtype=float) for i in mylist[1:]]
    city_num = 25
    dist = defaultdict(dict) #np.zeros((city_num, city_num))
    for i in range(city_num):
        for j in range(city_num):
            dist[i][j] = np.sqrt(np.sum((l[i] - l[j])**2))
    s=0
    for i in range(1, city_num+1):
        s = s|(1<<i) #2^25
    # path = np.ones((2 ** (city_num + 1), city_num))
    # dp = np.ones((2 ** (city_num + 1), city_num)) * -1
    dp = defaultdict(lambda :-1)
    distance=TSP3()
    # distance=TSP(s, 0)
    print(distance)
    # print(len(dp))
