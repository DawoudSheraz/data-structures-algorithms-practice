"""
Given an input integer array nums, write a function to find all unique triplets [nums[i], nums[j], nums[k]] such that i, j, and k are distinct indices,
and the sum of nums[i], nums[j], and nums[k] equals zero. Ensure that the resulting list does not contain any duplicate triplets.

Input:

nums = [-1,0,1,2,-1,-1]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: Both nums[0], nums[1], nums[2] and nums[1], nums[2], nums[4] both include [-1, 0, 1] and sum to 0.
nums[0], nums[3], nums[4] ([-1,-1,2]) also sum to 0.

Since we are looking for unique triplets, we can ignore the duplicate [-1, 0, 1] triplet and return [[-1, -1, 2], [-1, 0, 1]].

The order of the triplets and the order of the elements within the triplets do not matter.
"""

from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    result = []

    for counter in range(len(nums) - 2):
        # If the current element is same as previous, skip ahead to avoid duplicate triplets
        if counter > 0 and nums[counter] == nums[counter - 1]:
            continue
        left, right = counter + 1, len(nums) -1

        while left < right:
            current_sum = nums[counter] + nums[left] + nums[right]
            if current_sum == 0:
                # If the input array is not sorted, then this output result would need to be sorted
                # to be able to identify the duplicate triplets
                output_result = [nums[left], nums[counter], nums[right]]
                result.append(output_result)
                left += 1
                right -= 1

                # this is similar to check above, if the next element is same as previous, skip ahead to avoid duplicate triplets
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1
    return result


assert (three_sum([-1, 0, 1, 2, -1, -1])) == [[-1, -1, 2], [0, -1, 1]]
assert (three_sum([-1,0,1,2,-1,-4,-1,2,1])) == [[2, -4, 2], [-1, -1, 2], [0, -1, 1]]
