class Solution(object):
    
    def searchInsert(self,nums,target):
        for i, value in enumerate(nums):
            if value == target:
                return i 



sol = Solution()
print(sol.searchInsert([1,3,5,6], 5))
