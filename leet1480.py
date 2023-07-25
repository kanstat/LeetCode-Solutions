from typing import List
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
# Example 2:

# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
# Example 3:

# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]
nums = [1, 2, 3, 4]
# Output: [1, 1+2, 1+2+3, 1+2+3+4]. [1,3,6,10]


def runningSum(nums: List[int]) -> List[int]:
    n = len(nums)
    runng_sum = []
    for i in range(n):
        sum_ = 0

        for j in range(0, i+1):
            sum_ += nums[j]
        runng_sum.append(sum_)
    return runng_sum


def runningsum(nums):
    n = len(nums)
    r = 0
    runng_sum = []
    sum_ = 0
    while r < n:
        sum_ += nums[r]
        runng_sum.append(sum_)
        r += 1
    return runng_sum


print(runningSum(nums))
print(runningsum(nums))
