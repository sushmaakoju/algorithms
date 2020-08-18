def bubblesort(arr):
    """Always go from start to end until an element is not** greater than next element.
       avg, worst cases of complexity : O(n^2)

    Args:
        arr ([type]): list of unsorted elements
    """
    size = len(arr)
    for i in range(size):
        for j in range(0, size-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def cocktail_sort(arr):
    #instead of sorting top to bottom as in bubblesort, cocktail sort
    #sorts by alternating forward n backward passes.
    #Although worst n avg complexity cases are O(n^2),
    # suppose if elements are sorted to an index not too far from original index 
    # s.t differs k and k >=1, complexity is O(kn) ~ O(n).
    swapped = True
    size = len(arr)
    start = 0
    end = size - 1
    while swapped == True:

        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        if swapped == False:
            break
        swapped = True
        end -= 1
        for i in range(end-1, start-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        start += 1

def insertionsort(arr):
    "Recursive version"
    size = len(arr)
    return __insertionsort__(arr, size-1)

def __insertionsort__(arr, n):
    """Insertion sort. Worst case and avg case complexity O(n^2)
        recursive implementation.
    Args:
        arr ([type]): [description]
        n ([type]): [description]
    """
    if n > 0:
        __insertionsort__(arr, n-1)
    x = arr[n]
    j = n-1
    while j > 0 and arr[j] > x:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = x

def inserstion_sort(arr):
    #Iterative version
    i = 1
    while i < len(arr):
        x = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > x:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = x
        i += 1

def selectionsort(arr):
    #O(n^2)
    n = len(arr)
    for i in range(0, n-1):
        jmin = i
        for j in range(i+1, n):
            if arr[j] < arr[jmin]:
                jmin = j
        if jmin != i:
            a = arr[jmin], arr[i]   
            arr[i], arr[jmin] = a
        




