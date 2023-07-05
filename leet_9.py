# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

# method 1
def isPalindrome(x: int) -> bool:
    temp = x
    rev_no = 0
    while temp > 0:
        digit = temp % 10
        rev_no = digit+rev_no*10
        temp = temp//10
    if rev_no == x:
        return True
    else:
        return False


x = 121
print(isPalindrome(x))


# method 2

def ispanlindrome(x):
    x = str(x)
    if x == x[::-1]:
        return True
    else:
        False


print(ispanlindrome(x))
