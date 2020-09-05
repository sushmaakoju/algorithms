import math

def min_heapify(arr, i, heapsize):
    left = 2*i + 1
    right = 2*i +2
    smallest =  i
    if left < heapsize and arr[smallest] > arr[left]:
        smallest = left
    if right < heapsize and arr[smallest] > arr[right]:
        smallest = right
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, smallest, heapsize)
