'''
现有一个长度为n的序列，需要你求出最长的子序列，使得其长度最长，并且这个子序列是满足性质C的
子序列的定义：现有,则为一个子序列
性质C的定义：现有子序列，若,则称子序列满足性质C
'''

def getlen(men):
    if len(men)==0:
        return 0
    longest = {}
    longest[0] = 1
    for i in range(1, len(men)):
        maxlen = -1
        for j in range(0, i):
            if men[i] >=men[j] and maxlen < longest[j]:
                maxlen = longest[j]
        if maxlen >= 1:
            longest[i] = maxlen + 1
        else:
            longest[i] = 1
    return max(longest.values())
n = int(input())
men = list(map(int,input().split()))
print(getlen(men))


