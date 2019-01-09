from heapq import *


def insert(maxheap, minheap, num):
    if (len(maxheap) + len(minheap)) & 1:#总数为奇数插入最大堆
        if len(minheap) > 0:
            if num > minheap[0]:
                heappush(minheap, num)#新数据插入最小堆
                heappush(maxheap, -minheap[0])#最小堆中的最小插入最大堆
                heappop(minheap)
            else:
                heappush(maxheap, -num)
        else:
            heappush(maxheap, -num)
    else:#总数为偶数 插入最小堆
        if len(maxheap) > 0:
            if num < -maxheap[0]:
                heappush(maxheap, -num)#新数据插入最大堆
                heappush(minheap, -maxheap[0])#最大堆中的最大插入最小堆
                heappop(maxheap)
            else:
                heappush(minheap, num)
        else:
            heappush(minheap, num)


def getmedian(maxheap, minheap):
    if (len(maxheap) + len(minheap)) & 1:
        return minheap[0]
    else:
        return -maxheap[0]

if __name__ == '__main__':
    with open('week3.input', 'r') as f:
        mylist = f.readlines()
    l = [int(i.split('\n')[0]) for i in mylist]
    res = []
    maxheap = []
    minheap = []
    for num in l:
        insert(maxheap, minheap, num)
        # print(maxheap, minheap, getmedian(maxheap, minheap))
        res.append(getmedian(maxheap, minheap))
    print(sum(res)%10000)
