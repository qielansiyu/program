'''
#多关键字排序
#稳定排序方法，归并排序，从最低优先级关键字开始排序
4
2017 3 20 3
2016 2 20 0
2017 3 20 1
2016 3 21 2

'''
'''
n = int(input())
y=[]
m=[]
d=[]
arr=[]
for i in range(n):
    tmp = list(map(int,input().split()))
    y.append(tmp[0])
    m.append(tmp[1])
    d.append(tmp[2])
    arr.append(tmp[3])
matrix = zip(m,d,y,arr)
matrix = sorted(matrix,key=lambda x:(x[0],x[1],x[2],x[3]))
print(matrix)
'''

'''
def QuickSort(nums, l, r,index):
    n = len(nums)
    if l < r:
        m = partition(nums, l, r, index)
        QuickSort(nums, l, m, index)
        QuickSort(nums, m + 1, r, index)
    return nums


def partition(nums, l, r, index):
    m = nums[l]
    while l < r:
        while l < r and nums[r][index] >= m[index]:
            r -= 1
        nums[l] = nums[r]
        while l < r and nums[l][index] <= m[index]:
            l += 1
        nums[r]= nums[l]
    nums[l] = m
    return l
n = int(input())
matrix = []
for i in range(n):
    tmp = list(map(int, input().split()))
    matrix.append([tmp[1],tmp[2],tmp[0],tmp[3]])


#不稳定排序方法
matrix = QuickSort(matrix, 0, len(matrix)-1, 0)
#print(matrix)

l = 0
r = 0
for index in range(3):
    l = 0
    r = 0
    for i in range(1,n):
        if matrix[i][index] == matrix[i-1][index]:
            r += 1
        else:
            matrix = QuickSort(matrix, l, r, index+1)
            r = r + 1
            l = r
    matrix = QuickSort(matrix, l, r, index+1)
print(matrix)
'''
def merge_sort(li,index):
    #不断递归调用自己一直到拆分成成单个元素的时候就返回这个元素，不再拆分了
    if len(li) == 1:
        return li
    #取拆分的中间位置
    mid = len(li) // 2
    #拆分过后左右两侧子串
    left = li[:mid]
    right = li[mid:]
    #对拆分过后的左右再拆分 一直到只有一个元素为止
    #最后一次递归时候ll和lr都会接到一个元素的列表
    # 最后一次递归之前的ll和rl会接收到排好序的子序列
    ll = merge_sort(left,index)
    rl = merge_sort(right,index)
    # 我们对返回的两个拆分结果进行排序后合并再返回正确顺序的子列表
    # 这里我们调用拎一个函数帮助我们按顺序合并ll和lr
    return merge(ll,rl,index)
#这里接收两个列表
def merge(left ,right, index):
    # 从两个有顺序的列表里边依次取数据比较后放入result
    # 每次我们分别拿出两个列表中最小的数比较，把较小的放入result
    result = []
    while len(left)>0 and len(right)>0 :
        #为了保持稳定性，当遇到相等的时候优先把左侧的数放进结果列表，因为left本来也是大数列中比较靠左的
        if left[0][index] <= right[0][index]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    #while循环出来之后 说明其中一个数组没有数据了，我们把另一个数组添加到结果数组后面
    result += left
    result += right
    return result

n = int(input())
matrix = []
for i in range(n):
    tmp = list(map(int, input().split()))
    matrix.append([tmp[1],tmp[2],tmp[0],tmp[3]])
#稳定排序方法
for i in range(len(matrix[0])-1, -1, -1):
    matrix = merge_sort(matrix, i)
print(matrix)
