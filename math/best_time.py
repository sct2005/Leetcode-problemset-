
prices = [7,1,5,3,6,4]
def best_time(prices):
    best = 0 

    L = 0 

    for R in range(1, len(prices)):

        if prices[R] < prices[L]:
            L = R 
            
        else:
            best = max(best,(prices[R] - prices[L]))
    print(best)

        



best_time(prices)
