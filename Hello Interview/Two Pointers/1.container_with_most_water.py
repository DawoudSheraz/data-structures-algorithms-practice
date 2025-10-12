"""
Given an integer input array heights representing the heights of vertical lines,
write a function that returns the maximum area of water that can be contained by two of the lines (and the x-axis).
The function should take in an array of integers and return an integer.

#
#
#
#             |           |
#          |  +  -  -  -  +  -  |
#          |  +  -  +  +  +  -  |  |
#          |  +  +  +  +  +  +  |  |
heights = [3, 4, 1, 2, 2, 4, 1, 3, 2]
Output: 21
"""

from typing import List


class Solution:

    @staticmethod
    def max_area(heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        maximum_area = 0

        while left < right:
            height = min(heights[left], heights[right])
            width = right - left

            maximum_area = max(maximum_area, height * width)
            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1
        return maximum_area


assert Solution.max_area([3, 4, 1, 2, 2, 4, 1, 3, 2]) == 21
assert Solution.max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49