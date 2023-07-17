# Example 1:

# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.
# Example 2:

# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.
# Example 3:

# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.

s = "abciiidef"
k = 3

# brute force approach


def maxVowels(s: str, k: int) -> int:
    n = len(s)
    vowel = ['a', 'e', 'i', 'o', 'u']
    vowel_count = []
    for i in range(n):
        for j in range(i+1, n+1):
            x = s[i:j]
            if len(x) == k:
                count = 0
                for z in x:
                    if z in vowel:
                        count += 1
                vowel_count.append(count)
    return max(vowel_count)


print(maxVowels(s, k=3))
