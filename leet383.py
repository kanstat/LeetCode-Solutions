def canConstruct(ransomNote: str, magazine: str) -> bool:

    chars = dict()

    for i in ransomNote:
        if i in chars:
            chars[i] += 1
        else:
            chars[i] = 0

    for i in chars:
        if magazine.count(i) <= chars[i]:
            return False

    return True


ransomNote = "bg"
magazine = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"
print(canConstruct(ransomNote, magazine))
