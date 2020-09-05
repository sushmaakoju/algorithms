
def find_diff(a,b):
    count = 0
    for i in range(0, 32):
        if ((a >> i)&1) != ((b>>i)&1):
            count+=1
    return count

#n*n O(n^2)
def bruteforce_findall(arr, n):
    diff_count = 0
    for i in range(0,n):
        for j in range(0,n):
            diff_count += find_diff(arr[i], arr[j])
    print(diff_count)
    return diff_count

#O(n)
def better_diff(arr, n):
    tot = 0
    for i in range(0, 32):
        count = 0
        for j in range(0,n):
            if (arr[j] & (1 << i)):
                count+=1
        tot += count
    print(tot)

#given a real number between 0 and 1, print(binary representation)
def find_binary(num : float):
    if num >= 1 or num <=0:
        raise ValueError()
    bin_val = "."
    while num > 0 and len(bin_val) <= 32:
        r = num * 2
        if r >= 1:
            bin_val += "1"
            num = r - 1
        else:
            bin_val += "0"
            num = r
    return bin_val

print(find_diff(12,15))
print(find_diff(1,2))
bruteforce_findall([1,2], 2)
better_diff([1,2], 2)
better_diff([1,3,5], 3)
print(find_binary(0.72))
