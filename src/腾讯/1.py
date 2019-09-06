
def IsMagical(vec):
    le = len(vec)
    all = sum(vec)
    mid = all//2;
    dp = [0 for i in range(mid+1)]
    dp[0] = 1
    for i in range(le):
        for j in range(mid,0,-1):
            if (j >= vec[i]):
                dp[j] = max(dp[j], dp[j - vec[i]]);

    if (dp[mid]):
        print("YES")
    else:
        print('NO')
T = int(input())
for i in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    lis = {}
    for i in set(arr):
        lis[i] = arr.count(i)
    count = [lis[key] for key in lis]
    count = sorted(count)
    IsMagical(count)