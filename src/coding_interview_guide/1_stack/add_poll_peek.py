n = int(input())
operation = []
for i in range(n):
    operation.append(list(input().split()))
stackpush = []
stackpop = []
def add(data):
    stackpush.append(data)
def poll():
    try:
        if len(stackpop)==0:
            while(len(stackpush) != 0):
                stackpop.append(stackpush.pop())
        stackpop.pop()
    except:
        print('worry')

def peek():
    if len(stackpop) == 0:
        while (len(stackpush) != 0):
            stackpop.append(stackpush.pop())
    print(stackpop[-1])

for i in range(n):
    if operation[i][0]=='add':
        add(operation[i][1])
    elif operation[i][0]=='poll':
        poll()
    elif operation[i][0]=='peek':
        peek()



