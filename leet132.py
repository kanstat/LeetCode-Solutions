from typing import List
# Input: nums = [2,2,1]
# Output: 1
# Example 2:

# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:

# Input: nums = [1]
# Output: 1


def singleNumber(nums: List[int]) -> int:
    d = {}
    for i in nums:
        if i not in d:
            d[i] = 1
    else:
        d[i] += 1

    for key, val in d.items():
        if val == 1:
            return key


nums = [4, 1, 2, 1, 2]

print(singleNumber(nums))
