'''
题目描述
给定一个无序数组arr，其中元素可正、可负、可0。求arr所有子数组中正数与负数个数相等的最长子数组的长度。
[要求]
时间复杂度为O(n)O(n)，空间复杂度为O(n)O(n)
输入描述:
第一行一个整数N，表示数组长度
接下来一行有N个数表示数组中的数
输出描述:
输出一个整数表示答案
示例1
输入
5
1 -2 1 1 1
输出
2
'''

def sol():
    n = int(input())
    arr = list(map(lambda x: 1 if int(x) > 0 else -1, input().split()))
    res = 0
    rec = {0 : -1}
    k = 0
    count = 0
    for p in range(n):
        count += arr[p]
        if count not in rec:
            rec[count] = p
        if count - k in rec:
            res = max(res, p - rec[count - k])
    print(res)


if __name__ == "__main__":
    sol()

