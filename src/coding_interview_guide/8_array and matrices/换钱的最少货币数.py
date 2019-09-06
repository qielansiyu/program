'''
给定数组arr，arr中所有的值都为正整数且不重复。每个值代表一种面值的货币，每种面值的货币可以使用任意张，再给定一个aim，代表要找的钱数，求组成aim的最少货币数。
输入描述:
输入包括两行，第一行两个整数n（0<=n<=1000）代表数组长度和aim（0<=aim<=5000），第二行n个不重复的正整数，货币值

输出描述:
输出一个整数，表示组成aim的最小货币数，无解时输出-1.
示例1
输入
3 20
5 2 3
输出
4
'''
def seletc_coin(coin_arr, aim):
    dp = [0] + [float('inf')] * aim
    for i in range(1, aim + 1):
        for value in coin_arr:
            if value <= i and dp[i - value] + 1 < dp[i]:
                dp[i] = dp[i - value] + 1
    if dp[aim] == float('inf'):
        return -1
    else:
        return dp[aim]


n, aim = map(int, input().split())
arr = list(map(int, input().split()))
print(seletc_coin(arr, aim))