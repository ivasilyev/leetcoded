"""
Sort an Array

Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n))
time complexity and with the smallest space complexity possible.

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed
(for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).

Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.

Constraints:
    1 <= nums.length <= 5 * 104
    -5 * 104 <= nums[i] <= 5 * 104
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

    def sortArray(self, nums: list) -> list:
        self.heap_sort(nums)
        return nums
