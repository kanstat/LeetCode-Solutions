def printntimes(x=0):
    if x == 5:
        return
    print(x)
    printntimes(x+1)
    
    
    
printntimes()


def sumofdigits(n,sum):
    sum = sum+n
    if n == 0:
        return sum
    return sumofdigits(n-1,sum)
    
    
print(sumofdigits(5,0))