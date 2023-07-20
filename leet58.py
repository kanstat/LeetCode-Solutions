# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.

s = "   fly me   to   the moon  "
s = "luffy is still joyboy"


def lengthOfLastWord(s: str):
    x = s.split()
    w = x[-1]
    res = len(w)
    return res


print(lengthOfLastWord(s))
