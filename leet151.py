def reverseWords(s: str) -> str:
    s = s.split()
    l = 0
    r = len(s)-1
    while l <= r:
        temp = s[l]
        s[l] = s[r]
        s[r] = temp
        l += 1
        r -= 1
    s = ' '.join(s)
    return s


s = "the sky is blue"
print(reverseWords(s))
