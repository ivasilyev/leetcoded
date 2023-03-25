"""
Running Sum of 1d Array

Given an array nums. We define a running sum of an array as
runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]

Constraints:

1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
"""

class Solution:
    def runningSum(self, nums: list) -> list:
        if len(nums) < 2:
            return nums
        for idx in range(1, len(nums)):
            nums[idx] += nums[idx - 1]
        return nums

    def runningSum1(self, nums: list) -> list:
        c = 0
        for i in range(len(nums)):
            c += nums[i]
            nums[i] = int(c)
        return nums
