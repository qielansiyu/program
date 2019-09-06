'''
题目描述
给定一个无序数组arr, 其中元素可正、可负、可0。给定一个整数k，求arr所有子数组中累加和为k的最长子数组长度
输入描述:
第一行两个整数N, k。N表示数组长度，k的定义已在题目描述中给出
第二行N个整数表示数组内的数
输出描述:
输出一个整数表示答案
示例1
输入
5 0
1 -2 1 1 1
输出
3
'''
def sol():
    n, k = [int(i) for i in input().split(" ")]
    arr = [int(j) for j in input().split(" ")]
    res = 0
    rec = {0: -1}
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