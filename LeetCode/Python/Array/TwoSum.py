def twoSum(nums, target):
    ans = []

    for i in range(len(nums)):
        for j in range(i + 1,len(nums)):
            if nums[i] + nums[j] == target:
                ans = [i,j]
    return ans

print(twoSum([2,7,11,15], 9))
# where (nums, target)
