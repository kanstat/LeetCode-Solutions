# 1) Input:  txt[] = "BACDGABCDA"  pat[] = "ABCD"
#    Output:   Found at Index 0
#              Found at Index 5
#              Found at Index 6
# 2) Input: txt[] =  "AAABABAA" pat[] = "AABA"
#    Output:   Found at Index 0
#              Found at Index 1
#              Found at Index 4


def anagramstringsearch(text,pattern):
    n = len(text)
    m = len(pattern)
    
    pattern_list = [ele for ele in pattern]
    res = []
    
    for i in range(n-m+1):
        text_substring = [j for j in (text[i:i+m])]
        
        if set(pattern_list) == set(text_substring):
            res.append(i)
    return res
            
            
    
        

# s = 'BACDGABCDA'
# t = 'ABCD'
# li_t=[x for x in t]
# n=len(s)
# m=len(t)
# ans=[]

# for i in range(n-m+1):
#     li = [x for x in s[i:i+m]]
#     if set(li)==set(li_t):
#         ans.append(i)
# print(ans)
            
            

if __name__ == "__main__":
    text = "BACDGABCDA"
    pattern = "ABCD"
    
    
    # text = "AABAACAADAABAABA"
    # pattern = "AABA"
    
    print(anagramstringsearch(text,pattern))
    
    
    
            
            