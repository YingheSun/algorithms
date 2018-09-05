# -*- coding: utf-8 -*-

def heap(arr):
    # 排序节点
    def node_sort(_arr, _n, _N):
        print(arr)
        if _N < 2*_n:
            return
        elif _N == 2*_n:
            if _arr[_n] > _arr[2*_n]:
                _arr[_n], _arr[2*_n] = _arr[2*_n], _arr[_n]
        else:
            min_butree =  2*_n+1 if _arr[2*_n] > _arr[2*_n+1] else 2*_n
            if _arr[_n] > _arr[min_butree]:
                _arr[_n], _arr[min_butree] = _arr[min_butree], _arr[_n]
                node_sort(_arr, min_butree, _N)

    # 初始化得到最大堆
    N = len(arr) - 1
    for i in range(len(arr), 0, -1):
        node_sort(arr, i, N)

    # 堆顶与堆尾交换，下沉后重复得到从大到小排序
    for i in range(N-2):
        arr[1], arr[N-i] = arr[N-i], arr[1]
        node_sort(arr, 1, N-i-1)
    arr[1], arr[2] = arr[2], arr[1]


from random import randint
arr = [-1] + [randint(0, 1000) for i in range(20)]
print(arr)
heap(arr)
print(arr)