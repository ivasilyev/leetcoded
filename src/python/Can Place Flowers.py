"""
Can Place Flowers

You have a long flowerbed in which some of the plots are planted,
and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's,
where 0 means empty and 1 means not empty, and an integer n,
return if n new flowers can be planted in the flowerbed without violating
the no-adjacent-flowers rule.

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

Constraints:

    1 <= flowerbed.length <= 2 * 104
    flowerbed[i] is 0 or 1.
    There are no two adjacent flowers in flowerbed.
    0 <= n <= flowerbed.length

"""


class Solution:
    def canPlaceFlowers(self, flowerbed: list, n: int) -> bool:
        from re import findall
        flowerbed = "0{}0".format("".join([str(i) for i in flowerbed]))
        flowerbed = sum([(len(i) - 1) // 2 for i in findall("[0]{3,}", flowerbed)])
        return flowerbed >= n

    def canPlaceFlowers1(self, flowerbed: list, n: int) -> bool:
        flowerbed = [0, *flowerbed, 0]
        flowerbed_max_idx = len(flowerbed) - 1
        counter = 0
        zero_counter = 0
        for idx, i in enumerate(flowerbed):
            zero_counter += i == 0
            if i > 0 or idx == flowerbed_max_idx:
                if zero_counter > 2:
                    counter += (zero_counter - 1) // 2
                zero_counter = 0
        return counter >= n

    def canPlaceFlowers0(self, flowerbed: list, n: int) -> bool:
        flowerbed = [0, *flowerbed, 0]
        flowerbed_max_idx = len(flowerbed) - 1
        spaces = list()
        c = 0
        space = list()
        for idx, i in enumerate(flowerbed):
            if i == 0:
                space.append(i)
            if i > 0 or idx == flowerbed_max_idx:
                spaces.append(space)
                space = list()
        for i in spaces:
            zero_counter = len(i)
            if zero_counter > 2:
                c += (zero_counter - 1) // 2
        return c >= n

