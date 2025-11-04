"""
Write a function to sort a given integer array nums in-place (and without the built-in sort function),
where the array contains n integers that are either 0, 1, and 2 and represent the colors red, white, and blue.
Arrange the objects so that same-colored ones are adjacent, in the order of red, white, and blue (0, 1, 2).

Input: nums = [2,1,2,0,1,0,1,0,1]
Output: [0,0,0,1,1,1,1,2,2]
"""

from typing import List

def sort_colors(nums: List[int]) -> List[int]:

    left, right = 0, len(nums) - 1
    current = 0

    while current <= right:
        if nums[current] == 0:
            nums[current], nums[left] = nums[left], nums[current]
            left += 1
            current += 1
        elif nums[current] == 2:
            nums[current], nums[right] = nums[right], nums[current]
            # only right is decremented and current is not because anything between current
            # and right is unsorted and after exchange, moving current would result in incorrect array.
            right -= 1
        else:
            current += 1
        print(nums)

    return nums


print(sort_colors([2,1,2,0,1,0,1,0,1]))
