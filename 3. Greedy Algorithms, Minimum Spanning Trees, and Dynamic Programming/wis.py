if __name__ == '__main__':
    with open('mwis.txt', 'r') as f:
        mylist = f.readlines()
    l = [int(i.split('\n')[0]) for i in mylist[1:]]
    a = [0] * len(l)
    a[0] = l[0]
    a[1] = l[1]
    for i,v in enumerate(l[2:]):
        a[i+2] = max(a[i+1], a[i]+v)
    i = len(a)-1
    r = []
    while i>=0:
        if a[i-1] >= a[i-2] + l[i]:
            i -= 1
        else:
            r.append(i+1)
            i -= 2
    q = [1, 2, 3, 4, 17, 117, 517, 997]#q = [1, 2, 3, 4, 17, 117, 517, 997]
    d = set(r)
    print("".join(['1' if v in d else '0' for v in q]))#10100110