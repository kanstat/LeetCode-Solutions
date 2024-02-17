# 20. Valid Parentheses
# Solved
# Easy
# Topics
# Companies
# Hint
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false

def isValid(s: str) -> bool:
    dic = {")": "(", "}": "{", "]": "["}
    stack = []
    try:
        for i in s:
            if i in dic.values():
                stack.append(i)
            elif i in dic:
                close = dic[i]
                top = stack[-1]
                if close == top:
                    stack.pop()
                else:
                    return False
    except:
        return False
    if not stack:
        return True
    else:
        return False
    


s = "()[]{}]" 


print(isValid(s))