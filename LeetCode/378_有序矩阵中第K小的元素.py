# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 378. 有序矩阵中第K小的元素
Website: https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 248 ms, 在所有 Python3 提交中击败了54.70%的用户
Memory Usage: 19.9 MB, 在所有 Python3 提交中击败了50.00%的用户
=================================================="""


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        temp = []
        for i in matrix:
            temp.extend(i)
        temp.sort()
        return temp[k-1]

    def kthSmallest_2(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        pq = [(matrix[i][0], i, 0) for i in range(n)]
        heapq.heapify(pq)

        ret = 0
        for i in range(k - 1):
            num, x, y = heapq.heappop(pq)
            if y != n - 1:
                heapq.heappush(pq, (matrix[x][y + 1], x, y + 1))
        
        return heapq.heappop(pq)[0]
    '''
    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/solution/you-xu-ju-zhen-zhong-di-kxiao-de-yuan-su-by-leetco/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    '''

    def kthSmallest_3(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def check(mid):
            i, j = n - 1, 0
            num = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    num += i + 1
                    j += 1
                else:
                    i -= 1
            return num >= k

        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
    '''
    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/solution/you-xu-ju-zhen-zhong-di-kxiao-de-yuan-su-by-leetco/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    '''
