def Partition(nums,left,right):
    pivot = nums[left]; l = left + 1;r = right
    while (l <= r) :
        if (nums[l] > pivot and nums[r] < pivot):
            nums[l], nums[r] = nums[r],nums[l]
        if (nums[l] <= pivot): l+=1;
        if (nums[r] >= pivot): r-=1;
    nums[left], nums[r] = nums[r],nums[left]
    return r

def QuickSort(nums, lo, hi):
    if (hi <= lo): return;
    seg = Partition(nums, lo, hi)
    QuickSort(nums, lo, seg - 1)
    QuickSort(nums, seg + 1, hi)

if __name__=='__main__':
    n = int(input())
    all = list(input().split())
    nums = [0 for i in range(n)]
    ops = ['+' for i in range(n)]
    for i in range(n-1):
         nums[i] = int(all[2*i])
         ops[i+1] = all[2*i+1]
    nums[n - 1] = all[-1]

    l = 0; r = 0;
    while (r < n):
        while (r < n and ops[r] == ops[l]): r+=1;
        r-=1;
        if (ops[l] == '+' or ops[l] == '-'):
            if (r < n-1 and (ops[r+1] == '*' or ops[r+1] == '/')):
                QuickSort(nums, l, r-1)
            else:
                QuickSort(nums, l, r);

        elif (ops[l] == '*'):
            if (l > 0 and (ops[l-1] == '+' or ops[l-1] == '-')):
                QuickSort(nums, l-1, r);
            else:
                QuickSort(nums, l, r);
        elif (ops[l] == '/'):
            QuickSort(nums, l, r);
        r+=1
        l = r
    ans = str(nums[0])
    for i in range(1,n):
        ans+=' '
        ans+=ops[i]
        ans += ' '
        ans += str(nums[i])
    print(ans)
