from collections import Counter
# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,0,1,1,1,1,2,3,3]
# Output: 7, nums = [0,0,1,1,2,3,3,_,_]
# Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

nums = [1, 1, 1, 2, 2, 3]
#  5, nums = [1,1,2,2,3,_]
# nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]


def removeDuplicates(nums) -> int:
    count = 0
    n = len(nums)
    for i in range(1, n-1):
        if nums[i] == nums[i-1]:
            count += 1
        else:
            count = 0


def removeduplicates(nums) -> int:
    counter = Counter(nums)
    l = []
    for i, j in counter.items():
        if j > 2:
            l += [i]*2
        else:
            l += [i]*j
    nums[:] = l


def remove_duplicates(nums) -> int:
    for i in range(len(nums)-2, 0, -1):
        if (nums[i] == nums[i-1] and nums[i] == nums[i+1]):
            nums.pop(i+1)
    return len(nums)


print(remove_duplicates(nums))


def removedDuplicates(nums) -> int:
    i = 0
    for n in nums:
        if i < 2 or n > nums[i-2]:
            nums[i] = n
            i += 1
    return i


print(removedDuplicates(nums))
