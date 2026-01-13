
class Solution(object):
    nums = [1,2,3,4,5,6,7,8,9]
    def twosum(nums, target):
        for i in range(len(nums)):
            for k in range(i + 1, len(nums)):
                if nums[i] + nums[k] == target:
                    print(nums[i], nums[k])
                    return

    twosum(nums, 10)
