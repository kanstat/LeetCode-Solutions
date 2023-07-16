# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4

# def searchInsert(nums, target: int) -> int:
#     l = len(nums)
#     max_ = max(nums)
#     if target>max_:
#         return l+1
#     elif target not in nums:
#         for i in range(l):
#             if target<
#     for i in range(l):
#         if target == nums[i]:
#             return i
nums = [1, 3, 5, 6]
target = 7
nums = [1, 3, 5, 6]
target = 2


def searchInsert(nums, target: int) -> int:
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = left+(right-left)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left += 1
        else:
            right -= 1
    return left


print(searchInsert(nums, target))
