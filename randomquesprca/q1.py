# generate a question with input and output variales?
# Count the frequency of words appearing in a string Using Python

# input_string = "This is a test. This test is only a test."

# {
#     "this": 2,
#     "is": 2,
#     "a": 2,
#     "test": 3,
#     "only": 1
# }



def countwords(s):
    d = {}
    l = s.split()
    for item in l:
        if item not in d:
            d[item] = 1
        else:
            d[item] +=1
    return d

s = "This is a test. This test is only a test."

print(countwords(s))