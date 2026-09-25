



def reverse(x: int) -> int:
#define the valid signed 32 bit rnage 
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1 
    sign = -1 if x < 0 else 1 # going to sign it after reverse to avoid numerical issuses 
    x = abs(x)#absalute value as re signing it after 
    blank = 0 # our result 

#block of code while x isnt 0 we find the new digit by taking l;ast. digit of , multiplying curernt result by twn to "move it along" , then add next didgit 

    while x !=  0: 
        digit = x % 10 
        x = x // 10 
        blank = blank * 10 + digit
# once we are done we add the sign 
    blank *= sign 
# then check its in the rnage 

    if blank < INT_MIN or blank > INT_MAX:
        return 0

    return blank


print(reverse(-123))
