"""
Given an integer array nums, design an algorithm to randomly shuffle the array.
All permutations of the array should be equally likely as a result of the shuffling.

Implement the Solution class:

    Solution(int[] nums) Initializes the object with the integer array nums.
    int[] reset() Resets the array to its original configuration and returns it.
    int[] shuffle() Returns a random shuffling of the array.



Example 1:

Input
["Solution", "shuffle", "reset", "shuffle"]
[[[1, 2, 3]], [], [], []]
Output
[null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

Explanation
Solution solution = new Solution([1, 2, 3]);
solution.shuffle();    // Shuffle the array [1,2,3] and return its result.
                       // Any permutation of [1,2,3] must be equally likely to be returned.
                       // Example: return [3, 1, 2]
solution.reset();      // Resets the array back to its original configuration [1,2,3]. Return [1, 2, 3]
solution.shuffle();    // Returns the random shuffling of array [1,2,3]. Example: return [1, 3, 2]



Constraints:

    1 <= nums.length <= 50
    -106 <= nums[i] <= 106
    All the elements of nums are unique.
    At most 104 calls in total will be made to reset and shuffle.

   Hide Hint #1
The solution expects that we always use the original array to shuffle() else some of the test cases fail.
(Credits; @snehasingh31)
"""

from random import randint


class Solution:

    def __init__(self, nums: list):
        self._nums = nums

    def reset(self) -> list:
        return self._nums

    def shuffle(self) -> list:
        indexes = list()
        r = randint(0, len(self._nums) - 1)
        for _ in range(len(self._nums)):
            while r in indexes:
                r = randint(0, len(self._nums) - 1)
            indexes.append(r)
        return [self._nums[idx] for idx in indexes]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()