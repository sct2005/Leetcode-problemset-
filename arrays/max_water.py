height = [1,8,6,2,5,4,8,3,7]

def most_water(height):
    best = 0
    L = 0
    R = len(height) - 1

    while L < R:
        x_axis = R - L
        y_axis = min(height[L], height[R])
        result = x_axis * y_axis
        best = max(best, result)

        if height[L] < height[R]:
            L += 1
        else:
            R -= 1

    print(best)


most_water(height)
