# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

nums = [2, 10, 11, 15, 7]
target = 9


def twoSum(nums, target: int):
    l = len(nums)
    for i in range(l):
        for j in range(i+1, l):
            if nums[i]+nums[j] == target:
                return [i, j]


print(twoSum(nums, target))
