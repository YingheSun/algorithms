# -*- coding: utf-8 -*-

import random
def radixSort(A):
    print(A)
    for k in range(4):  #4轮排序(对应最大的数字的位数)
        s=[[] for i in range(10)]
        for i in A:
            s[int(i/(10**k)%10)].append(i)
        A=[a for b in s for a in b]
    return A

print(radixSort([random.randint(1,9999) for i in range(10)]))