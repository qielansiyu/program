'''
输入1：
3 2
1 3
2 3
4 4
'''
t,k = map(int,input().split())
a = []
b = []
for i in range(t):
    tmp = list(map(int, input().split()))
    a.append(tmp[0])
    b.append(tmp[1])
max_b = max(b)
arr = [1 for i in range(max_b+1)]
if k == 1:
    for i in range(1,max_b+1):
        arr[i]=arr[i-1]*2
else:
    for i in range(k,max_b+1):
        arr[i]=arr[i-1]+arr[i-k]

for i in range(t):
    result = sum(arr[a[i]:b[i]+1])
    print(result)
