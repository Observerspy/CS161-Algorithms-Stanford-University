import numpy as np

if __name__ == '__main__':
    with open('knapsack.txt', 'r') as f:
        mylist = f.readlines()
    l = [np.array(i.split('\n')[0].split(' '), dtype=int) for i in mylist[1:]]
    a = np.zeros((100, 10000))
    a[0] = [l[0][0] if l[0][1] < i else 0 for i in range(10000)]
    for i in range(1, 100):
        for j in range(10000):
            if j >= l[i][1]:
                a[i,j] = max(a[i-1,j], a[i-1,j-l[i][1]]+l[i][0])
            else:
                a[i, j] = a[i-1,j]
    print(a[-1,-1])#2493893