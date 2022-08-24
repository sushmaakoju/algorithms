#Quick sort
def quicksort(arr, lo, hi):
    """quick sort using lomuto partition

    Args:
        arr ([type]): [description]
        lo ([type]): [description]
        hi ([type]): [description]
    """
    if lo < hi:
        p = lomuto_partition(arr, lo, hi)
        quicksort(arr, lo, p-1)
        quicksort(arr, p+1, hi)

def quicksort_hp(arr, lo, hi):
    """quick sort using hoare partition

    Args:
        arr ([type]): [description]
        lo ([type]): [description]
        hi ([type]): [description]
    """
    if lo < hi:
        p = hoare_partition(arr, lo, hi)
        quicksort_hp(arr, lo, p)
        quicksort_hp(arr, p+1, hi)
    

def lomuto_partition(arr, lo, hi):
    #pick pivot to be last element element (if list is already sorted just O(n^2)
    #for unsorted list, time complexity is still O(n^2)
    pivot = arr[hi]
    i = lo - 1
    for j in range(lo, hi):
        if arr[j] < pivot:
            i += 1
            a = arr[j], arr[i] 
            arr[i], arr[j] = a
    a = arr[i+1], arr[hi]
    arr[hi], arr[i+1] = a
    return i

def hoare_partition(arr, lo, hi):
    #pick pivot to be middle element (if list is already sorted O(nlog(n) < O(n^2))))
    #for unsorted list, time complexity is still O(n^2)
    pivot = (arr[hi] + arr[lo])//2
    i = lo - 1
    j = hi + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        a = arr[i], arr[j]
        arr[j], arr[i] = a
    print(arr)

# END - Quick sort
