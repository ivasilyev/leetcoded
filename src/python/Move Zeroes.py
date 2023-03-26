"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:

Input: nums = [0]
Output: [0]

Constraints:

    1 <= nums.length <= 104
    -2**(31) <= nums[i] <= 2**(31) - 1
"""


class Solution:
    def moveZeroes(self, nums: list):
        """
        Do not return anything, modify nums in-place instead.
        """
        insert_position = 0
        for idx, i in enumerate(nums):
            if i != 0:
                nums[insert_position] = i
                insert_position += 1

        while insert_position < len(nums):
            nums[insert_position] = 0
            insert_position += 1
