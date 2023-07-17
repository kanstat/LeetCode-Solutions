# Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
# Output: "leetcode"
# Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
# Example 2:

# Input: s = "abc", indices = [0,1,2]
# Output: "abc"
# Explanation: After shuffling, each character remains in its position.


s = "codeleet"

indices = [4, 5, 6, 7, 0, 2, 1, 3]


def restoreString(s: str, indices) -> str:
    n = len(s)
    l = [0]*n
    for i in range(n):
        l[indices[i]] = s[i]
    s = ''.join(l)
    return s


print(restoreString(s, indices))
