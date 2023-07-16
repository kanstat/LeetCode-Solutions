# Write a Python function to find all the anagrams in a given list of words. An anagram is a word or phrase formed by
# rearranging the letters of another word or phrase. The function should take a list of words as input and return a
# list of lists, where each inner list contains a group of words that are anagrams of each other.


# Input: ["listen", "silent", "pot", "top", "part", "trap", "hello", "world"]
# Output: [["listen", "silent"], ["pot", "top"], ["part", "trap"], ["hello"], ["world"]]
lst = ["listen", "silent", "pot", "top", "part", "trap", "hello", "world"]


# def func(lst):
#     n = len(lst)
#     ana = []
#     for i in range(n):
#         sub_ana = []
#         for j in range(n):
#             i_sort = sorted(lst[i])
#             j_sort = sorted(lst[j])
#             if i_sort == j_sort:
#                 sub_ana.append(lst[j])
#         ana.append(sub_ana)
#     # s = list[set(ana)]
#     return ana


# print(func(Input))


def anagrams_func(lst):
    d = {}
    for word in lst:
        key = ''.join(sorted(word))
        if key in d:
            d[key].append(word)
        else:
            d[key] = [word]
    return [group for group in d.values()]


print(anagrams_func(lst))
