#最长递增子序列的最小字典序输出
n = int(input().split()[0])
arr = list(map(int, input().split()))
def lengthofLIS(arr):
    lens = len(arr)
    # tails[i]为所有长度为i + 1的递增子序列的最小的尾元素，tails是一个递增的数组
    # 递增子序列的最大长度也就是当前tails数组中所能到达的最右侧的位置
    tails = [0] * lens
    # dp[i]表示遍历到arr[i]时，arr[0...i]组成的最长子序列长度
    dp = [1] * lens
    # maxindex[i]用来保存tails[i]在原数组中的下标
    maxindex = [0] * lens
    tails[0] = arr[0]
    maxlen = 1
    for k in range(1, lens):
        # 如果需要求的是非严格单调递增数组，只需要把arr[k] > tails[maxlen]改为arr[k] >= tails[maxlen]即可
        if arr[k] > tails[maxlen - 1]:
            tails[maxlen] = arr[k]
            maxindex[maxlen] = k
            maxlen += 1
            dp[k] = maxlen
        else:
            i = 0
            j = maxlen
            # 通过二分查找，维护tails中的元素，保证每次对于长度为i+1的一个子序列对应的tails[i]元素最小
            while i < j:
                # 防止溢出
                mid = i + (j - i) // 2
                if tails[mid] < arr[k]:
                    i = mid + 1
                else:
                    j = mid
            tails[i] = arr[k]
            dp[k] = i + 1
            if i == maxlen - 1:
                maxindex[i] = k
    LIS = [0] * maxlen
    index = maxindex[maxlen - 1]
    k = maxlen - 1
    LIS[k] = arr[index]
    for i in range(maxindex[maxlen - 1])[::-1]:
        if arr[i] < arr[index] and (dp[i] == dp[index] - 1):
            k -= 1
            LIS[k] = arr[i]
            index = i
    for i in range(maxlen):
        print(LIS[i], end=" ")
    return maxlen
lengthofLIS(arr)