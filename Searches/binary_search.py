nums = [1,2,3,4,5,6,7,8,9]

def binary_search(nums, key):
    low = 0 
    high = len(nums) - 1
    while low < high:

        mid = low + (high - low) //2

        if nums[mid] == key:
            return mid

        elif nums[mid] < key:
            low = mid + 1

        else: 
            high = mid - 1
    return - 1 

binary_search(nums, 2)
