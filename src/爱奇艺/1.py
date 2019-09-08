def fun(arr):
    tmp = pow(10,9)+7
    dp = [[0 for i in range(len(arr)+1)] for j in range(len(arr)+1)]
    dp[0][0]=1
    for i in range(len(arr)):
        if arr[i]==1:
            for j in range(1,i+2):
                dp[i+1][j]=(dp[i+1][j-1]+dp[i][j-1])%tmp
        else:
            for j in range(i,-1,-1):
                dp[i+1][j]=(dp[i+1][j+1]+dp[i][j])%tmp
    res = 0
    for i in range(len(arr)+1):
        res=(res+dp[len(arr)][i])%tmp
    return res
N = int(input())
arr = list(map(int,input().split()))
print(fun(arr))
