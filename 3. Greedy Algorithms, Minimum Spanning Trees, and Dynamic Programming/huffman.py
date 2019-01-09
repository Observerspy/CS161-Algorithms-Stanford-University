class Node():
    def __init__(self, weight):
        self.weight = weight
        self.left = None
        self.right = None

def huffman(a):
    l = [Node(v) for v in a]
    while len(l) > 1:
        l.sort(key=lambda node: node.weight, reverse=False)
        n = Node(l[0].weight + l[1].weight)
        n.left = l.pop(0)
        n.right = l.pop(0)
        l.append(n)
    return l[0]

def getlength(root, l):
    global min_deep, max_deep
    if not root:
        if l > max_deep:
            max_deep = l
        if l < min_deep:
            min_deep = l
        return
    getlength(root.left, l+1)
    getlength(root.right, l+1)


max_deep = 0
min_deep = 1000
if __name__ == '__main__':
    with open('huffman.txt', 'r') as f:
        mylist = f.readlines()
    l = [int(i.split('\n')[0]) for i in mylist[1:]]
    root = huffman(l)
    getlength(root, 0)
    print(max_deep-1, min_deep-1)#19 9
