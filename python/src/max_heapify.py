import math

def max_heapify(arr, i, heapsize):
    left = 2*i + 1
    right = 2*i +2
    largest =  i
    if left < heapsize and arr[largest] < arr[left]:
        largest = left
    if right < heapsize and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, heapsize)
