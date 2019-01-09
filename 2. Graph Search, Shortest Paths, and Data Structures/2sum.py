from tqdm import tqdm,trange
def find(number, array, flag='up'):
    """ binary search. """
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = array[mid]
        if guess == number:
            return mid
        elif guess < number:
            low = mid + 1
        else: #guess > number
            high = mid - 1
    if flag == 'up':
        return low
    if flag == 'low':
        return high


if __name__ == '__main__':
    with open('week4.input', 'r') as f:
        mylist = f.readlines()
    l = [int(i.split('\n')[0]) for i in mylist]
    l = sorted(set(l))
    res = set()
    for num in tqdm(l):
        low = find(-10000-num, l)
        hi = find(10000-num, l, flag='low')
        res.update([num+i for i in l[low:hi+1] if num != i])
        # if len(l[low:hi])>1:
        #     print(-10000-num, 10000-num, l[low-1:hi+2])
    print(len(res))#427