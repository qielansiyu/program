#前序遍历递归方法
def preOrderRecur(node):
    if node==None:
        return
    print(node.value)
    pre(node.left)
    pre(node.right)

def preOrderUnRecur(head):
    if head!=Node:
        stack = []
        stack.append(head)
        while(len(stack)!=0):
            head = stack.pop()
            if head.right!=None:
                stack.append(head.right)
            if(head.left!=None):
                stack.append(head.left)
            print(head)