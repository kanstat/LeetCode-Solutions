arr = [1,2,4,5,6,7]


def summation(arr):
    n = len(arr)+1
    sonn = (n*(n+1))//2
    missingnum = sonn-sum(arr)
    return missingnum



print(summation(arr))