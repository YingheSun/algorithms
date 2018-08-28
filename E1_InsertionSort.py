def insertSortNormal(arr):
    length = len(arr)
    for j in range(2, length):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i = i - 1
        arr[i+1] = key

def printArr(arr):
    for item in arr:
        print(item)

arr = [4, 7 ,8 ,2 ,3 ,5]
insertSortNormal(arr)
printArr(arr)
