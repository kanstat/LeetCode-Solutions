from typing import List
# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# method 1 hashing


def containsDuplicate(nums: List[int]) -> bool:
    d = {}
    for i in nums:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    for val in d.values():
        if val > 1:
            return True
    return False


nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
# Output: true


# method 2
def containDuplicate(nums: List[int]) -> bool:
    s = sorted(nums)
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    return False


# method 3
def containDuplicat(nums: List[int]) -> bool:
    visited = []
    for i in nums:
        if i not in nums:
            visited.append(i)
        else:
            return True
    return False


print(containsDuplicate(nums))
print(containDuplicate(nums))
print(containDuplicat(nums))
