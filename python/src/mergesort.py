
def mergesort(arr):
    if len(arr) <= 1:
        return arr
    
    size = len(arr)
    left = list()
    right = list()
    for i in range(0, size):
        if i < size//2:
            left.append(arr[i])
        else:
            right.append(arr[i])
    
    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)

def merge(left, right):
    result = list()
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result