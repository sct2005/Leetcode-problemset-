nums = [1, 2, 3,1]

seen = []

count = 0 

while count < len(nums):

    if nums[count] in seen:
        print("False")
        break

    seen.append(nums[count])
    count += 1 



else:
    print("True")




