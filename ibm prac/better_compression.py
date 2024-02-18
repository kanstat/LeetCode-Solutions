s = "a3c9b2c1"

def better_comp(s):
    d = {}
    i=0
    while i<len(s):
        char =  s[i] 
        freq = int(s[i+1])
        d[char] = d.get(char,0)+freq
        i+=2
        
    res = ""
    for key in sorted(d.keys()):
        res+=key+str(d[key])
    print(res)
        
        
        
better_comp(s)