from .mergesort import *
def timsort(arr):
    #O(nlog(n))
    RUN  = 32
    n = len(arr)
    for i in range(0, n, 32):
        binary_insertionsort(arr, i, min((i+31), (n-1)))
    size = RUN
    while size < n:
        for left in range(0,n, 2*size ):
            mid = left + size -1
            right = min((left + 2*size -1), (n-1))
            merge_run(arr, left, mid, right)
        size = 2*size

def binary_insertionsort(arr, left, right):
    for i in range(left+1, right+1):
        x = arr[i]
        j = i - 1
        while j >= left and arr[j] > x:
            arr[j+1] =  arr[j]
            j -= 1
        arr[j+1] = x

def merge_run(arr, l, m, r):
    len1, len2 = m-l+1, r-m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[i])
    for j in range(0, len2):
        right.append(arr[j])
    
    merge(left, right)
