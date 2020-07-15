# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 96. 不同的二叉搜索树
Website: https://leetcode-cn.com/problems/unique-binary-search-trees/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 32 ms, 在所有 Python3 提交中击败了95.27%的用户
Memory Usage: 13.5 MB, 在所有 Python3 提交中击败了5.26%的用户
=================================================="""


class Solution:
    """
    给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
    """

    calculate = {0: 1, 1: 1, 2: 2}

    def numTrees(self, n: int) -> int:
        if n == 0:
            return 1
        
        res = 0
        for i in range(1, n + 1):
            if i - 1 in self.calculate:
                left = self.calculate[i - 1]
            else:
                left = self.numTrees(i - 1)
                self.calculate[i - 1] = left

            if n - i in self.calculate:
                right = self.calculate[n - i]
            else:
                right = self.numTrees(n - i)
                self.calculate[n - i] = right
            
            res += left * right
        return res

    def numTrees_2(self, n):
        """
        :type n: int
        :rtype: int
        """
        G = [0]*(n+1)
        G[0], G[1] = 1, 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1] * G[i-j]

        return G[n]
    """
    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/unique-binary-search-trees/solution/bu-tong-de-er-cha-sou-suo-shu-by-leetcode-solution/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """

    def numTrees_3(self, n):
        """
        :type n: int
        :rtype: int
        
        卡塔兰数
        """
        C = 1
        for i in range(0, n):
            C = C * 2*(2*i+1)/(i+2)
        return int(C)
    # 作者：LeetCode-Solution
    # 链接：https://leetcode-cn.com/problems/unique-binary-search-trees/solution/bu-tong-de-er-cha-sou-suo-shu-by-leetcode-solution/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    def numTrees_4(self, n: int) -> int:
        return int(math.factorial(2*n)/math.factorial(n+1)/math.factorial(n))
