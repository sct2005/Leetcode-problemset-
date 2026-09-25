
s = "abcabcbb"


L = 0 
best = ""
window = ""
for R in range(1,len(s)):

    while s[R] in window: 
        window = window[1:]
        L += 1 
    window += s[R]

    if len(window) > len(best):
        best = window

print(best)

    
        


