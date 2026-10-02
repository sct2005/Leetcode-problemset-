nums = [3,5,6,7,8,8,9]


def majority_element(nums):
    seen = {}

    for i in nums:
        

        if i in seen:
            seen[i] += 1
        else:
            seen[i] = 1
    majority = max(seen, key = seen.get)


    return majority

print(majority_element(nums))
