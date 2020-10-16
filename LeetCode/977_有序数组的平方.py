# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 977. 有序数组的平方
Website: https://leetcode-cn.com/problems/squares-of-a-sorted-array/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 260 ms, 在所有 Python3 提交中击败了86.53%的用户
Memory Usage: 15.5 MB, 在所有 Python3 提交中击败了5.22%的用户
=================================================="""


class Solution:
    """
    给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。
    """
    def sortedSquares(self, A: List[int]) -> List[int]:
        A = [abs(i) for i in A]
        A.sort()
        return [i**2 for i in A]

    def sortedSquares2(self, A: List[int]) -> List[int]:
        return sorted(num * num for num in A)

    def sortedSquares3(self, A: List[int]) -> List[int]:
        n = len(A)
        negative = -1
        for i, num in enumerate(A):
            if num < 0:
                negative = i
            else:
                break

        ans = list()
        i, j = negative, negative + 1
        while i >= 0 or j < n:
            if i < 0:
                ans.append(A[j] * A[j])
                j += 1
            elif j == n:
                ans.append(A[i] * A[i])
                i -= 1
            elif A[i] * A[i] < A[j] * A[j]:
                ans.append(A[i] * A[i])
                i -= 1
            else:
                ans.append(A[j] * A[j])
                j += 1

        return ans

    def sortedSquares4(self, A: List[int]) -> List[int]:
        n = len(A)
        ans = [0] * n
        
        i, j, pos = 0, n - 1, n - 1
        while i <= j:
            if A[i] * A[i] > A[j] * A[j]:
                ans[pos] = A[i] * A[i]
                i += 1
            else:
                ans[pos] = A[j] * A[j]
                j -= 1
            pos -= 1
        
        return ans


# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/squares-of-a-sorted-array/solution/you-xu-shu-zu-de-ping-fang-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
