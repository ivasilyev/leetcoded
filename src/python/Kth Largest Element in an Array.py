"""
Kth Largest Element in an Array

Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
You must solve it in O(n) time complexity.

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:
    1 <= k <= nums.length <= 105
    -104 <= nums[i] <= 104
"""


class Solution:
    def heap_sort(self, lst: list) -> None:
        """
        Mutates elements in lst by utilizing the heap data structure
        """
        def max_heapify(heap_size, index):
            left, right = 2 * index + 1, 2 * index + 2
            largest = index
            if left < heap_size and lst[left] > lst[largest]:
                largest = left
            if right < heap_size and lst[right] > lst[largest]:
                largest = right
            if largest != index:
                lst[index], lst[largest] = lst[largest], lst[index]
                max_heapify(heap_size, largest)

        # heapify original lst
        for i in range(len(lst) // 2 - 1, -1, -1):
            max_heapify(len(lst), i)

        # use heap to sort elements
        for i in range(len(lst) - 1, 0, -1):
            # swap last element with first element
            lst[i], lst[0] = lst[0], lst[i]
            # note that we reduce the heap size by 1 every iteration
            max_heapify(i, 0)

    def findKthLargest(self, nums: list, k: int) -> int:
        self.heap_sort(nums)
        return nums[-k]
