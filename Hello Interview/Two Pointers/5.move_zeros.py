"""
Given an integer array nums, write a function to rearrange the array by moving all zeros to the end while keeping the order of non-zero elements unchanged.
Perform this operation in-place without creating a copy of the array.

Input: nums = [2,0,4,0,9]
Output: [2,4,9,0,0]
"""

from typing import List

def move_zeroes(nums: List[int]) -> List[int]:

    if len(nums) == 0:
        return nums

    non_zero_index = 0
    for idx in range(len(nums)):
        if nums[idx] != 0:
            nums[non_zero_index] = nums[idx]
            non_zero_index += 1

    # Fill the remaining list with 0s, which is essentially moving the zeros to the end
    for idx in range(non_zero_index, len(nums)):
        nums[idx] = 0

    return nums


print(move_zeroes([2,0,4,0,9,0]))
print(move_zeroes([0, 1, 0, 2, 0, 3]))
