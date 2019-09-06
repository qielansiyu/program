#时间复杂度O(n2)
def getdp1(arr):
    dp = [1 for i in range(n)]
    for i in range(n):
        for j in range(i):
            if arr[i]>arr[j]:
                dp[i] = max(dp[i],dp[j]+1)
    return dp

def generateLIS(arr,dp):
    len = max(dp)
    index = dp.index(max(dp))
    lis = [0 for i in range(len)]
    len -=1
    lis[len] = arr[index]
    for i in range(index,-1,-1):
        if (arr[i]<arr[index] and dp[i]==dp[index]-1):
            len -= 1
            lis[len] = arr[i]
            index = i
    return lis
if __name__=='__main__':
    n = int(input())
    arr = list(map(int,input().split()))
    lis = generateLIS(arr,getdp1(arr))
    for i in lis:
        print(i, end=' ')




