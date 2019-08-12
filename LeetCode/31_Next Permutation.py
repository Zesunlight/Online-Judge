"""
    Problem: 31. Next Permutation
    Website: https://leetcode.com/problems/next-permutation/
    Author: ZYZ
    Language: Python3
    Result: Accepted
    Runtime: 52 ms, faster than 51.43% of Python3 online submissions for Next Permutation.
    Memory Usage: 13.6 MB, less than 5.56% of Python3 online submissions for Next Permutation.
"""


class Solution:
    """
    Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

    If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

    The replacement must be in-place and use only constant extra memory.

    Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

    1,2,3 → 1,3,2
    3,2,1 → 1,2,3
    1,1,5 → 1,5,1
    """

    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        adjust = False
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                for j in range(len(nums) - 1, -1, -1):
                    if nums[j] > nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        break

                b = sorted(nums[i + 1:])
                nums[i + 1:] = b
                # more effieient way after reading discusses
                # b = nums[i + 1:]
                # b.reverse()
                # nums[i + 1:] = b
                adjust = True
                break

        if not adjust:
            nums.reverse()


s = Solution()
a = [4, 2, 0, 2, 3, 2, 0]
print(s.nextPermutation(a))
print(a)


"""
https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
https://leetcode.com/problems/next-permutation/discuss/13867/C++-from-Wikipedia

Find the largest index k such that nums[k] < nums[k + 1]. If no such index exists, just reverse nums and done.
Find the largest index l > k such that nums[k] < nums[l].
Swap nums[k] and nums[l].
Reverse the sub-array nums[k + 1:].
"""