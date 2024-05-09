# Text: AABAACAADAABAABA
# Pattern: AABA

# Output: Pattern Found at 0, 9 and 12 index



def patternfinding(text,pattern):
    n = len(text)
    m = len(pattern)
    
    for i in range(n-m+1):
        j = 0
        
        while j < m  and text[i+j] == pattern[j]:
            j+=1
            

        if j == m:
            print(f"found pattern at {i}")
            
            
            
if __name__ == "__main__":
    text = "AABAACAADAABAABA"
    
    pattern = "AABA"
    
    
    patternfinding(text,pattern)
    