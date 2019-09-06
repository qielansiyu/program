#矩阵最小路径和
n,m = map(int,input().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int,input().split())))
def minPathSum1(m):
    row = len(m)
    col = len(m[0])
    dp = [[0 for i in range(col)] for i in range(row)]
    dp[0][0] = m[0][0]
    for i in range(1,row):
        dp[i][0] = dp[i-1][0] + m[i][0]
    for j in range(1,col):
        dp[0][j] = dp[0][j-1] + m[0][j]
    for i in range(1,row):
        for j in range(1,col):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + m[i][j]
    return(dp[row-1][col-1])
print(minPathSum1(matrix))

