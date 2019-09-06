N = int(input())
X = list(map(int,input().split()))
def getAndRemoveLastElement(stack):
    result = stack.pop()
    if len(stack) == 0:
        return result
    else:
        last = getAndRemoveLastElement(stack)
        stack.append(result)
        return last

def reverse(stack):
    if len(stack)==0:
        return(stack)
    else:
        i = getAndRemoveLastElement(stack)
        stack = reverse(stack)
        stack.append(i)
        return(stack)
X = reverse(X)
for i in X:
    print(i,end=' ')

