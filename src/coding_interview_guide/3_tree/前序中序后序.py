class Tree:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right



def build_tree(t):
    for i in range(n):
        if t.val == data[i][0]:
            if data[i][1]!=0:
                t.left = Tree(data[i][1])
                t = build_tree(t.left)
                print(t.val)
            if data[i][2] !=0:
                t.right = Tree(data[i][2])
                t = build_tree(t.right)
                print(head.val)
            return
    return

def pre_traverse(node):
    if node.value == None:
        return
    print(node.value)
    pre_traverse(node.left)
    pre_traverse(node.right)
    return
if __name__ == '__main__':
    tmp = list(map(int, input().split()))
    n = tmp[0]
    head = tmp[1]
    head = Tree(head)
    root = head
    data = []
    for i in range(n):
        data.append(list(map(int, input().split())))
    #build_tree(head)
    #pre_traverse(head)
    for i in range(n):
        if head.val == data[i][0]:
            if data[i][1]!=0:
                head.left = Tree(data[i][1])
                head = head.left
    print(head.left.val)
'''
3 1
1 2 3
2 0 0
3 0 0
'''