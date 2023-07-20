from typing import List
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
# Example 2:

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
# Example 3:

# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].


def plusOne(digits: List[int]) -> List[int]:
    strs = ''
    for digit in digits:
        strs += str(digit)
    int_strs = int(strs)+1
    strs = str(int_strs)
    digits = []
    for i in strs:
        digits.append(int(i))

    return digits


digits = [9]
print(plusOne(digits))
