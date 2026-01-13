
import math

class Solution(object):




    def palidrome(x): 
        if x < 0:
            return False
        original = x 
        reversed_num = 0
        while x > 0:
            reversed_num = reversed_num * 10 +  (x % 10)
            x = x // 10 
        if reversed_num == original:
            print("the number is a palidrome")
        else:
            print("the number is not an palidrome")

    palidrome(121)
