

def max_sub_array_sum(nums):
    if not nums:
        return 0
    
    current_sum = global_sum = nums[0]
    
    for n in nums[1:]:
        current_sum = max(n,current_sum+n)
        if current_sum > global_sum:
            global_sum = current_sum
            
    return global_sum



    
    

    
    
    
    
    
    
    
    
if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(max_sub_array_sum(nums))
    
    
    