#选择最远距离*2+锻炼效果相加 AC=0.6
'''
5
1 2 3 4 5
1 2 3 4 5
'''
N = int(input())
dists = list(map(int, input().split(' ')))
es = list(map(int, input().split(' ')))

dists_es = list(zip(dists, es))
dists_es.sort(key=lambda x: (x[0],x[1]))
#print(dists_es)
dp = []
for k in range(N):
    tmp = [-1 for i in range(N)]
    dp.append(tmp)

weights = [2 * dists_es[i][0] + dists_es[i][1] for i in range(N)]
helper_max = [0 for i in range(N)]
tmp_max = 0
for i in range(N):
    if i == 0:
        dp[0] = weights
    else:
        tmp_max = dp[i - 1][-1]
        #tmp_max = max(dp[i-1])
        helper_max[-1] = tmp_max

        h = N - 2
        while h >= 0:
            tmp_max = max(tmp_max, dp[i - 1][h])
            helper_max[h] = tmp_max
            h -= 1
        print(helper_max)
        for j in range(N - i):
            dp[i][j] = dists_es[j][1] + helper_max[j + 1]  # max(dp[i-1][j+1:])

    print(max(dp[i]))

print(dp)