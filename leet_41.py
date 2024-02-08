# 41. First Missing Positive
# Hard
# Topics
# Companies
# Hint
# Given an unsorted integer array nums, return the smallest missing positive integer.

# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

# Example 1:

# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.
# Example 2:

# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.
# Example 3:

# Input: nums = [7,8,9,11,12]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.



def firstMissingPositive(nums):
    # if len(nums)==1 and nums[0]<1 or nums[0]==0:
    #     return 1
    # if len(nums)==1 and nums[0]>1:
    #     return 1
    # if len(nums)==1 and nums[0]==1:
    #     return nums[0]+1
    # sorted_nums = sorted(nums)
    # max_num = max(sorted_nums)
    # for i in range(1,max_num+2): #3----1,2
    #     if i not in sorted_nums:
    #         return i
    unique = set(nums)
    i = 1
    while i in unique:
        i += 1
    return i
    
nums = [1]

if __name__ == "__main__":
    print(firstMissingPositive(nums))