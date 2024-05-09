# Input: nums = [1,5,4,2,9,9,9], k = 3
# Output: 15



def check_duplicates(nums):
    seen = []
    for i in nums:
        if i in seen:
            return False
        seen.append(i)
    return True
            

def maxsubarray(nums,k):
    n = len(nums)
    max_sum = 0
    for i in range(n-k+1):
        substrofsizek = [x for x in nums[i:i+k]]
        ans = check_duplicates(substrofsizek)
        if ans == True:
            sum_ = sum(substrofsizek)
            max_sum = max(sum_,max_sum)
    return max_sum
        
        

nums = [1,5,4,2,9,9,9]

k = 3


print(maxsubarray(nums,k))