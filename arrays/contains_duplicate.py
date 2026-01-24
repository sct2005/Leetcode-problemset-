nums = [1,2,3,1]

def containsDuplicate(nums):
    seen = set()
    for num in nums: 
        if num in seen:
            
            return True 
        seen.add(num)
    return False    

containsDuplicate(nums)

#use a hash set instead of an double for loop thi stakes time complexity from O(n^2) to O(n)
