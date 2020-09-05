def tripletSum(nums: list) -> [[list]]:
        nums.sort()
        results = []
        keys = {e:i for i,e in enumerate(nums)}
        for i in range(0, len(nums)):
            j = i+1
            while j < len(nums) and i!=j:
                this_sum = -(nums[i] + nums[j])
                if this_sum in keys and keys[this_sum] != i and keys[this_sum] != j:
                    triplet = [nums[i] , nums[j], this_sum]
                    if sum([1 for v in results if sorted(v) != sorted(triplet)]) == len(results):
                        results.append((nums[i] , nums[j], this_sum))
                j -= 1
        return results

print(tripletSum( [-1, 0, 1, 2, -1, -4]))