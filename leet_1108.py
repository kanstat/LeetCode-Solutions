def defangIPaddr(address: str) -> str:
    address = address.replace('.', '[.]')
    return address

# Example 1:

# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"
# Example 2:

# Input: address = "255.100.50.0"
# Output: "255[.]100[.]50[.]0"


address = "1.1.1.1"

print(defangIPaddr(address))
