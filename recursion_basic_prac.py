# def printntimes(x=0):
#     if x == 5:
#         return
#     print(x)
#     printntimes(x+1)
    
    
    
# printntimes()


# def sumofdigits(n,sum):
#     sum = sum+n
#     if n == 0:
#         return sum
#     return sumofdigits(n-1,sum)
    
    
# print(sumofdigits(5,0))

def sumdigits(n):
    if n == 0:
        return 0
    return (n%10) + sumdigits(n//10)

    
# print(sumdigits(1234))

def fibonancci(n):
    if n==0 or n ==1:
        return n
    return fibonancci(n-1) + fibonancci(n-2)

# n = int(input())
# for n in range(0,n):
    # print(fibonancci(n),end=' ')

def reverse_list(li,l,r):
    if l>=r:
        return li
    li[l], li[r] = li[r], li[l]
    return reverse_list(li, l+1, r-1)


# li = [1,2,3,4,2]
# n = len(li)
# rev_li = reverse_list(li, 0, n-1)
# print(rev_li)


def print1ton(n):
    if n==0:
        return
    print(n,end="  ")
    return print1ton(n-1)


# print1ton(10)


def factorial_calculation(n:int):
    if n == 0:
        return 1
    return n * factorial_calculation(n-1)


# print(factorial_calculation(5))



def isPalRec(st, s, e) :
     
    # If there is only one character
    if (s == e):
        return True
 

    if (st[s] != st[e]) :
        return False
 
 
    if (s < e + 1) :
         return isPalRec(st, s + 1, e - 1);
 
    return True

st = "malyalam"
print(isPalRec(st,0,len(st)-1))