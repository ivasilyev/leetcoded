"""
Sort Colors

Given an array nums with n objects colored red, white, or blue,
sort them in-place so that objects of the same color are adjacent,
with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]

Constraints:

    n == nums.length
    1 <= n <= 300
    nums[i] is either 0, 1, or 2.

Follow up: Could you come up with a one-pass algorithm using only constant extra space?
   Hide Hint #1
A rather straight forward solution is a two-pass algorithm using counting sort.
   Hide Hint #2
Iterate the array counting number of 0's, 1's, and 2's.
   Hide Hint #3
Overwrite array with the total number of 0's, then 1's and followed by 2's.
"""


class Solution:
    def selection_sort(self, lst: list) -> None:
        """
        Mutates lst so that it is sorted via selecting the minimum element and
        swapping it with the corresponding index
        """
        for i in range(len(lst)):
            min_index = i
            for j in range(i + 1, len(lst)):
                # Update minimum index
                if lst[j] < lst[min_index]:
                    min_index = j

            # Swap current index with minimum element in rest of list
            lst[min_index], lst[i] = lst[i], lst[min_index]

    def sortColors(self, nums: list) -> None:
        self.selection_sort(nums)

    def sortColors1(self, nums: list) -> None:
        # Bubble Sort
        """
        Do not return anything, modify nums in-place instead.
        """
        c = 1
        while c > 0:
            c = 0
            for idx in range(len(nums) - 1):
                next_idx = idx + 1
                if nums[idx] > nums[next_idx]:
                    nums[idx] ^= nums[next_idx]
                    nums[next_idx] ^= nums[idx]
                    nums[idx] ^= nums[next_idx]
                    c += 1
