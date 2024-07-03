# Write a Python function to find all pairs of integers in an array that add up to a given sum. The function should have a time complexity of 
# O(n).


array = [1, 5, 7, -1, 5]
target_sum = 6

# -1,1,5,5,7
def find_sum(arr,target):
    res = []
    arr.sort()
    l = len(arr)
    left = 0
    right = l-1
    
    while left<=right:
        if target < arr[left] + arr[right]:
            left = left+1
        elif target > arr[left] + arr[right]:
            right = right-1
        elif target == arr[left] + arr[right]:
            res.append((arr[left], arr[right]))
            right=right-1
            left=left+1
    return res


print(find_sum(array,target_sum))