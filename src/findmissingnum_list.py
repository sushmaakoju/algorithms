#O(N) , N is size of list of all elements from 1 to max(arr)
def bruteforce(arr):
    result = [element for element in range(max(arr)+1) if element not in arr ]
    return result

#def optimal_sol(arr):
    
print(bruteforce([3,5,6,8,10]))