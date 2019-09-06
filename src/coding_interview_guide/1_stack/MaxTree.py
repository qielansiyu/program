# 构造数组的MaxTree
from array import array


class Node:
    """二叉树节点"""

    def __init__(self, data):
        self.left = None
        self.right = None
        self.value = data


def getMaxTree(arr: array) -> Node:
    nArr = [Node(i) for i in arr]
    stack = []
    lBigMap = {}
    rBigMap = {}

    # 找出所有节点左边最大的数对应的节点
    for i in range(len(arr)):
        curNode = nArr[i]
        while stack and stack[-1].value < curNode.value:
            popStackSetMap(stack, lBigMap)
        stack.append(curNode)

    while stack:
        popStackSetMap(stack, lBigMap)

    # 找出所有节点右边最大的数对应的节点
    for i in range(len(arr) - 1, -1, -1):
        curNode = nArr[i]
        while stack and stack[-1].value < curNode.value:
            popStackSetMap(stack, rBigMap)
        stack.append(curNode)

    while stack:
        popStackSetMap(stack, rBigMap)

    # 将节点构建成二叉树（head对应为完整的二叉树，其他为子树）
    head = None
    for i in range(len(nArr)):
        curNode = nArr[i]
        left = lBigMap[curNode]
        right = rBigMap[curNode]
        if left == None and right == None:
            head = curNode
        elif left == None:
            if right.left == None:  # 先判断父节点左端是否有节点，没有的话接上当前节点
                right.left = curNode  # 此特性决定了该二叉树往往左偏
            else:
                right.right = curNode
        elif right == None:
            if left.left == None:
                left.left = curNode
            else:
                left.right = curNode
        else:
            parent = left if left.value < right.value else right
            if parent.left == None:
                parent.left = curNode
            else:
                parent.right = curNode
    return head


def popStackSetMap(stack: list, map_: dict):
    """
    将节点对应的数字在数组中左或者右最大的数字对应的节点形成映射
    """
    popNode = stack.pop()
    if not stack:
        map_[popNode] = None
    else:
        map_[popNode] = stack[-1]


if __name__ == "__main__":
    arr = array('i', [3, 4, 5, 1, 2])
    head = getMaxTree(arr)