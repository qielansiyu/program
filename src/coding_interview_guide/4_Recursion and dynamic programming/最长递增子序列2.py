#O(nlogn),求长度
def lengthOfLIS(nums):
    size = len(nums)
    if size < 2:
        return size
    cell = [nums[0]]
    for num in nums[1:]:
        if num > cell[-1]:
            cell.append(num)
            continue
        l, r = 0, len(cell) - 1
        while l < r:
            mid = l + (r - l) // 2
            if cell[mid] < num:
                l = mid + 1
            else:
                r = mid
        cell[l] = num
    return len(cell)

if __name__=='__main__':
    n = int(input())
    arr = list(map(int,input().split()))
    print(lengthOfLIS(arr))