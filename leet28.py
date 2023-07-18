# import re

# # string = 'sadbutsad'
# string = 'leetcode'
# # substring = 'sad'
# # substring = 'o'
# # match = re.search(substring, string)

# # if match:
# #     start = match.start()
# #     end = match.end()
# #     print(f'Substring found from index {start} to {end - 1}')
# # else:
# #     print('Substring not found')


# # ind = string.index(substring)
# # print(ind)
# # haystack = "sadbutsad"
# # needle = "sad"
# def find_substring(string, substring):
#     string_len = len(string)
#     substring_len = len(substring)

#     for i in range(string_len - substring_len + 1):
#         found = True
#         for j in range(substring_len):
#             if string[j] != substring[j]:
#                 found = False
#                 break
#         if found:
#             return i

#     return -1


# # Example usage
# # string = "Hello, world!"
# # substring = "world"
# index = find_substring(string, substring)
# if index != -1:
#     print("Substring found at index:", index)
# else:
#     print("Substring not found!")

def find_substring(string, substring):
    string_len = len(string)
    substring_len = len(substring)

    for i in range(string_len - substring_len + 1):
        found = True
        for j in range(substring_len):
            if string[i + j] != substring[j]:
                found = False
                break
        if found:
            return i

    return -1


# Example usage
string = "hello"
substring = "ll"

index = find_substring(string, substring)
if index != -1:
    print("Substring found at index:", index)
else:
    print("Substring not found!")
