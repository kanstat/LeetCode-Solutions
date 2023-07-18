# Example 1:

# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Example 2:

# Input: s = "God Ding"
# Output: "doG gniD"

def reverseWords(s: str) -> str:
    x = s.split()
    l = []
    for word in x:
        word = word[::-1]
        l.append(word)
    s = ' '.join(l)
    return s


s = "Let's take LeetCode contest"
print(reverseWords(s))
