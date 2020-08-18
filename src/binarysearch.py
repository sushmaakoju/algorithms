from .exception import *

#Pseudocode
# compare x with middle element in sorted list
# if element ==  middle element, return index
# else if element > middle element, recur binary search for l, middleelement index-1
# else recur seach for middleelement index -1 , r
class BinarySearch():
    
    def binary_search(self, arr, element):
        l = 0
        r = len(arr) - 1
        return self.__binarysearch__(arr, element, l, r)

    def __binarysearch__(self, arr, element, l=0 , r=0):
        mid = l + (r-l)//2
        if r >= l:
            if element == arr[mid] :
                return mid
            elif element > arr[mid]:
                return self.__binarysearch__(arr, element, mid+1, r)
            else:
                return self.__binarysearch__(arr, element, l, mid-1)
        else:
            return -1
    
    #def binarytree_binarysearch(self, id, node : TreeNode, ):
        
            