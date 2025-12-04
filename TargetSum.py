def twoSum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        rem = target - num
        if rem in seen:
            return [seen[rem], i]

        seen[num] = i

    return []


print(twoSum([2,7,11,15], 9))   
