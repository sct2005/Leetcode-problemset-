def two_sum(nums: list,target: int) -> list:

    seen = {}

    for index, num in enumerate(nums):
        complement = target - num 

        if complement in seen:
            print([num,complement])
            return True

        else:
            seen[num] = index

    print(seen)
    return False

two_sum([2,7,11,15],9)
