#Sliding window 
#your not recluclating sums from scratch  = slow 
# there will be some same elemnts 
#for sum ones subtract leacing elemnt from sum and add jopinning element to sum , window can be any size 
import time

#Brute force 
prices = [5,6,7,8,9,10,3,4,7,9,1,2]
def best_total_price(prices, k):  #num of prices 
    start = time.time()
    maxtotal = 0 

    for i in range(len(prices)-k+1):  
        total = sum(prices[i:i+k])
        maxtotal = max(maxtotal, total)
    end = time.time()
    print(f"{maxtotal},{(end - start)}")


# sliding window 
def best_total_price_window(prices, k):
    start = time.time()
    total = sum (prices[:k])#sum of the first k lements of the array 
    maxtotal = total
    for i in range(len(prices)-k):
        total -= prices[i]#subtract elemt at i , this is our leaving element
        total += prices[i+k]#add our next elemnt 

        #why i and i + k , i is the curerent index in first rotaion it will be 0 , so window if k = 5 , 0,1,2,3,4  , 0 + 5 = 5 , next elemnt = 5 33

        maxtotal = max(maxtotal, total)
    end = time.time()
    print(f"{maxtotal},{(end - start)}")
    return maxtotal

best_total_price_window(prices,5)


