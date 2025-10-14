"""
Write a function to count the number of triplets in an integer array nums that could form the sides of a triangle.
The triplets do not need to be unique.

Input: nums = [11,4,9,6,15,18]
Output: 10
Explanation: Valid combinations are...

4, 15, 18
6, 15, 18
9, 15, 18
11, 15, 18
9, 11, 18
6, 11, 15
9, 11, 15
4, 6, 9
"""

from typing import List, Tuple


def triangle_number(heights: List[int]):
    triangle_triplets: List[Tuple[int, int, int]] = []
    heights.sort()
    n = len(heights)
    for count in range(2, n):
        # Fix the largest one on third position and then use two pointes to find pairs before it.
        # I was doing this  wrong before, where right pointer was being set to count - 1 in every iteration of the outer loop.
        # which did not "fix" the largest one on third position.
        left, right = 0, count - 1

        while left < right:
            if heights[left] + heights[right] > heights[count]:
                for inner_counter in range(left, right):
                    triangle_triplets.append((heights[count], heights[inner_counter], heights[right]))
                right -= 1
            else:
                left += 1
    return len(triangle_triplets)


print(triangle_number([11, 4, 9, 6, 15, 18]))
print(triangle_number([3,4,1,2,2,4,1,3,2]))  # 39
