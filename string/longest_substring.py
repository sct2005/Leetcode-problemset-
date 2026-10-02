
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

    



s = "abcabcbb"
def longest_substring(s: str) -> str:

    longest = ""
    current = ""
    L = 0 

    for R in range(1,len(s)):

        while s[R] in current:
            current = current[1:]

            L += 1 
        current += s[R]

        if len(current) > len(longest):
            longest = current
    return longest



longest_substring(s)


