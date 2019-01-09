def InversionNum(lst):
    # 改写归并排序,在归并排序中，每当R部分元素先于L部分元素插入原列表时，逆序对数要加L剩余元素数
    if len(lst) == 1:
        return lst, 0
    else:
        n = len(lst) // 2
        lst1, count1 = InversionNum(lst[0:n])
        lst2, count2 = InversionNum(lst[n:len(lst)])
        lst, count = Count(lst1, lst2, 0)
        return lst, count1 + count2 + count


def Count(lst1, lst2, count):
    i = 0
    j = 0
    res = []
    while i < len(lst1) and j < len(lst2):
        if lst1[i] <= lst2[j]:
            res.append(lst1[i])
            i += 1
        else:
            res.append(lst2[j])
            count += len(lst1) - i  # 当右半部分的元素先于左半部分元素进入有序列表时，逆序对数量增加左半部分剩余的元素数
            j += 1
    res += lst1[i:]
    res += lst2[j:]
    return res, count

if __name__ == '__main__':
    with open('week2.input', 'r') as f:
        list = f.readlines()
    l = [int(i.split('\n')[0]) for i in list]
    _, res = InversionNum(l)
    print(res)