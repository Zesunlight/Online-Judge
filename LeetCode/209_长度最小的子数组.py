# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 209. 长度最小的子数组
Website: https://leetcode-cn.com/problems/minimum-size-subarray-sum/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 64 ms, 在所有 Python3 提交中击败了39.43%的用户
Memory Usage: 17.7 MB, 在所有 Python3 提交中击败了11.11%的用户
=================================================="""


class Solution:
    """
    给定一个含有 n 个正整数的数组和一个正整数 s ，
    找出该数组中满足其和 ≥ s 的长度最小的连续子数组，并返回其长度。
    如果不存在符合条件的连续子数组，返回 0。
    """
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        include = [0 for _ in range(len(nums))]
        part_sum = [0 for _ in range(len(nums))]
        res = 0
        if not nums:
            return 0
        part_sum[0] = nums[0]
        include[0] = 1
        if nums[0] == s:
            return 1
        if nums[0] > s:
            res = 1

        for i in range(1, len(nums)):
            if nums[i] > s:
                include[i] = 1
                res = 1
                part_sum[i] = nums[i]
            elif nums[i] == s:
                return 1
            else:
                part_sum[i] = part_sum[i - 1] + nums[i]
                include[i] = include[i - 1] + 1
                if part_sum[i] >= s:
                    while part_sum[i] - nums[i - include[i] + 1] >= s:
                        part_sum[i] -= nums[i - include[i] + 1]
                        include[i] -= 1

                    if res != 0:
                        res = min(res, include[i])
                    else:
                        res = include[i]
        return res

    def minSubArrayLen_2(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        ans = n + 1
        sums = [0]
        for i in range(n):
            sums.append(sums[-1] + nums[i])
        
        for i in range(1, n + 1):
            target = s + sums[i - 1]
            bound = bisect.bisect_left(sums, target)
            if bound != len(sums):
                ans = min(ans, bound - (i - 1))
        
        return 0 if ans == n + 1 else ans
    """
    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/minimum-size-subarray-sum/solution/chang-du-zui-xiao-de-zi-shu-zu-by-leetcode-solutio/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def minSubArrayLen_3(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        ans = n + 1
        start, end = 0, 0
        total = 0
        while end < n:
            total += nums[end]
            while total >= s:
                ans = min(ans, end - start + 1)
                total -= nums[start]
                start += 1
            end += 1
        
        return 0 if ans == n + 1 else ans
    '''
    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/minimum-size-subarray-sum/solution/chang-du-zui-xiao-de-zi-shu-zu-by-leetcode-solutio/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    '''
