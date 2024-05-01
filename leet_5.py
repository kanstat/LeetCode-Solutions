# Given a string s, return the longest 
# palindromic
 
# substring
#  in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"

def longest_palindrome(s):
    l = len(s)
    max_pal = ""
    for i in range(l):
        for j in range(i+1,l+1):
            sub = s[i:j]
            print(f"substring: {sub}")
            if sub == sub[::-1] and len(sub)>len(max_pal):
                max_pal = sub
    return max_pal
                
    

    



if __name__ == "__main__":
    s = "babad"
    print(longest_palindrome(s))
            
            