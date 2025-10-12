"""
Given a sorted array of integers nums, determine if there exists a pair of numbers that sum to a given target.

Example 1:
Input:
nums = [1,3,4,6,8,10,13]
target = 13
Output: True # (3 + 10 = 13)

Example 2:
Input:
nums = [1,3,4,6,8,10,13]
target = 6
Output: False
"""

from typing import List

def two_sum(nums: List[int], target: int) -> bool:
    left, right = 0, len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return True

        # Since array is sorted, the pointer area adjusted based on the current sum.
        # If greater than target, then moving left ahead would mean a larger sum (sorted array, right is already large).
        # that's why right pointer is moved left in that case.
        if current_sum > target:
            right -= 1
        else:
            left += 1
    return False


assert two_sum(nums=[1, 3, 4, 6, 8, 10, 13], target=13) == True
assert two_sum(nums=[1, 3, 4, 6, 8, 10, 13], target=6) == False
assert two_sum(nums=[-5, -3, 0, 2, 4, 6, 8], target=1) == True