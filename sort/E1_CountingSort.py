import random
def countingSort(alist,k):
    n=len(alist)
    b=[0 for i in range(n)]
    c=[0 for i in range(k+1)]
    for i in alist:
        c[i]+=1
    for i in range(1,len(c)):
        c[i]=c[i-1]+c[i]
    for i in alist:
        b[c[i]-1]=i
        c[i]-=1
    return b
if __name__=='__main__':
    a=[random.randint(0,20) for i in range(20)]
    print(countingSort(a,20))