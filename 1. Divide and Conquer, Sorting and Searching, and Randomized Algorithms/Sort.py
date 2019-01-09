count = 0


def choosemiddle(a, l, r):
    mid = 0
    if (r-l+1) % 2 == 0:
        mid = l + (r-l+1)//2 -1
    else:
        mid = l + (r-l+1)//2
    if (a[mid] - a[l]) * (a[mid] - a[r]) < 0:
        return mid
    elif (a[l] - a[mid]) * (a[l] - a[r]) < 0:
        return l
    else:
        return r


def partition(a, l, r):
    global count
    # pi = l #choose first 162085
    # pi = r #choose last 164123
    pi = choosemiddle(a, l, r) #choose middle 138382
    if pi != l:
        swap(a, pi, l)

    p = a[l]
    i = l+1
    for j in range(l+1, r+1):
        if a[j] < p:
            swap(a, j, i)
            # count += 1
            i += 1
    swap(a, l, i-1)
    count += r-l
    return i-1


def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


def quickSort(a, l, r):
    if l >= r:
        return
    pos = partition(a, l, r)
    quickSort(a, l, pos - 1)
    quickSort(a, pos + 1, r)


if __name__ == '__main__':
    with open('week3.input', 'r') as f:
        list = f.readlines()
    a = [int(i.split('\n')[0]) for i in list]
    # a = [2, 20, 1, 15, 3, 11, 13, 6, 16, 10, 19, 5, 4, 9, 8, 14, 18, 17, 7, 12]
    quickSort(a, 0, len(a)-1)
    print(count)