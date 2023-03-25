"""
Sort Array By Parity

Given an integer array nums, move all the even integers at the
beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Example 2:

Input: nums = [0]
Output: [0]

Constraints:

    1 <= nums.length <= 5000
    0 <= nums[i] <= 5000
"""


class Solution:
    def sortArrayByParity(self, nums: list) -> list:
        arr_1 = list()
        arr_2 = list()
        for i in nums:
            if i % 2 == 0:
                arr_2.append(i)
            else:
                arr_1.append(i)
        return arr_2 + arr_1

    def sortArrayByParity1(self, nums: list) -> list:
        c = 1
        while c > 0:
            c = 0
            for idx in range(len(nums) - 1):
                next_idx = idx + 1
                if nums[idx] % 2 > 0 and nums[next_idx] % 2 == 0:
                    nums[idx] ^= nums[next_idx]
                    nums[next_idx] ^= nums[idx]
                    nums[idx] ^= nums[next_idx]
                    c += 1
        return nums
