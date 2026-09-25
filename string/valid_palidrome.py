s = "A man, a plan, a canal: Panama"
result = ''.join(char for char in s if char.isalpha())
result = result.lower()
L = 0 
R = (len(result) - 1)
while L < R:
    if result[L] != result[R]:
        
        print("False")
        break

    L+=1
    R-=1
else:
    print("True")
