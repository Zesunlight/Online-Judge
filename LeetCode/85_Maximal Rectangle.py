"""
    Problem: 85. Maximal Rectangle
    Website: https://leetcode.com/problems/maximal-rectangle/
    Difficulty: Hard
    Author: ZYZ
    Language: Python3
    Result: Accepted
    Runtime: 128 ms, faster than 44.57% of Python3 online submissions for Largest Rectangle in Histogram.
    Memory Usage: 15.6 MB, less than 9.09% of Python3 online submissions for Largest Rectangle in Histogram.
"""


class Solution:
    """
    Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
    """

    def maximalRectangle(self, matrix) -> int:
        if len(matrix) == 0:
            return 0

        visited = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        area = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0' or visited[i][j] == 1:
                    continue
                else:
                    pass

        return 0


s = Solution()
a = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
    ]
print(s.maximalRectangle(a))
