# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 974. 和可被 K 整除的子数组
Website: https://leetcode-cn.com/problems/subarray-sums-divisible-by-k/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 416 ms, 在所有 Python3 提交中击败了38.58%的用户
Memory Usage: 17.5 MB, 在所有 Python3 提交中击败了100.00%的用户
=================================================="""


class Solution:
    """
    给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。
    """
    def subarraySum(self, A, K: int) -> int:
        if A is None or len(A) == 0:
            return 0
        sub_sum = {0: 1}
        s = 0
        amount = 0
        for i in range(len(A)):
            s += A[i]
            if K == 0:
                if s - K in sub_sum:
                    amount += sub_sum[s - K]
                sub_sum[s] = sub_sum.get(s, 0) + 1
            else:
                if (s - K) % K in sub_sum:
                    amount += sub_sum[(s - K) % K]
                sub_sum[s % K] = sub_sum.get(s % K, 0) + 1

        return amount


s = Solution()
print(s.subarraySum([4,5,0,-2,-3,1], -2))

"""
https://leetcode-cn.com/problems/subarray-sum-equals-k/solution/he-wei-kde-zi-shu-zu-by-leetcode-solution/
前缀和 + 哈希表优化

https://leetcode-cn.com/problems/subarray-sums-divisible-by-k/solution/he-ke-bei-k-zheng-chu-de-zi-shu-zu-by-leetcode-sol/
我们令 P[i] = A[0] + A[1] + ... + A[i]
那么每个连续子数组的和 sum(i,j) 就可以写成 P[j] - P[i-1]（其中 0 < i < j）的形式。
此时，判断子数组的和能否被 K 整除就等价于判断 (P[j] - P[i-1]) mod K == 0，
根据 同余定理，只要 P[j] mod K == P[i-1] mod K，就可以保证上面的等式成立。
"""
