
n = 4

def ways(n):
    steps = 0 
    if n == 1:
        
        return 1 
    elif n == 2: 
        
        return 2  
    else:
        
        return ways(n-1) + ways(n-2)




print(ways(n))
