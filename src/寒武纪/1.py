'''
1 10
-1 4 0 3 -3 -2 -3 -2 5 1
'''
N, M = map(int, input().split())
matrix = []
for i in range(N):
    matrix.append(list(map(int,input().split())))
dp = [0 for i in range(M)]
dp[0] = matrix[0][0]
for i in range(1, M):
        #状态转移方程
        dp[i] = max(matrix[0][i], dp[i-1] + matrix[0][i])
        #求最大连续子序列和
k = dp[0]
for i in range(M):
    if(dp[i] > k):
        k = dp[i]
print(k)     #输出
