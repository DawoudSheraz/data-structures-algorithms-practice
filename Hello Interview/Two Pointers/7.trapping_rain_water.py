"""
Write a function to calculate the total amount of water trapped between bars on an elevation map, where each bar's width is 1.
The input is given as an array of n non-negative integers height representing the height of each bar.

Input:

# .  .  .  .  .  x  .  .  .
# .  x  .  .  .  x  .  .  .
# x  x  .  .  .  x  .  .  .
# x  x  .  x  x  x  .  .  x
# x  x  x  x  x  x  x  .  x
# ==================================
height = [3, 4, 1, 2, 2, 5, 1, 0, 2]
Output: 10
"""

from typing import List


def trapping_water(height: List[int]) -> int:

    if not height:
        return 0

    output = 0
    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0

    while left <= right:
        # To store the water at any index, we need to know the high position on its left and right.
        # the minimum of the heights on either side - current height gives the amount of water stored.
        if right_max < left_max:
            if height[right] > right_max:
                right_max = height[right]
            else:
                output += right_max - height[right]
            right -= 1
        else:
            if height[left] > left_max:
                left_max = height[left]
            else:
                output += left_max - height[left]
            left += 1
    return output


print(trapping_water([3, 4, 1, 2, 2, 5, 1, 0, 2]))
print(trapping_water([4,2,0,3,2,5]))  # 9
print(trapping_water([0,1,0,2,1,0,1,3,2,1,2,1]))  #6
