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
    start = 0
    end = len(nums)-1
    while (start <= end):
        middle = (start+end)//2
        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            end = end - 1
        else:
            start += 1
    return start


print(searchInsert(nums, target))
