def buildMaxHeap(arr):
    for i in range(len(arr)//2,-1,-1):
        heapify(arr,i)
def swap(arr, i, j):
    arr[i],arr[j] = arr[j], arr[i]

def heapify(arr, i):
    left = 2*i+1
    right = 2*i +2
    largest = i
    if left < arrLen and arr[left] > arr[largest]:
        largest = left
    if right < arrLen and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        swap(arr, i, largest)
        heapify(arr, largest)


def heapsort(arr):
    global arrLen
    arrLen = len(arr)
    buildMaxHeap(arr)
    for i in range(len(arr)-1, 0, -1):
        swap(arr,0,i)
        arrLen -=1
        heapify(arr,0)
    return arr
arr=[7,6,5,4,3,2,1]
print(heapsort(arr))