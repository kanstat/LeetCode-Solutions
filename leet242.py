# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false

def isAnagram(s: str, t: str) -> bool:
    s = ''.join(sorted(s))
    t = ''.join(sorted(t))
    return (s == t)


s = "anagram"
t = "nagaram"
print(isAnagram(s, t))
