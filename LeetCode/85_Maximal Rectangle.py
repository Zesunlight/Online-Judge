# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 85. 最大矩形
Website: https://leetcode-cn.com/problems/maximal-rectangle/
Difficulty: Hard
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 160 ms, 在所有 Python3 提交中击败了38.57%的用户
Memory Usage: 14.8 MB, 在所有 Python3 提交中击败了12.50%的用户
=================================================="""


class Solution:
    "给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。"
    def maximalRectangle(self, matrix) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        left = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        right = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        height = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        res = 0

        for index in range(len(matrix[0])):
            if matrix[0][index] == "0":
                right[0][index] = len(matrix[0])
            else:
                if index == 0:
                    pass
                elif matrix[0][index - 1] == "0":
                    left[0][index] = index
                else:
                    left[0][index] = left[0][index - 1]
                height[0][index] = 1

            if matrix[0][-index - 1] == "1":
                if index == 0:
                    right[0][len(matrix[0]) - index - 1] = len(matrix[0]) - index - 1
                else:
                    right[0][len(matrix[0]) - index - 1] = right[0][len(matrix[0]) - index] \
                        if matrix[0][len(matrix[0]) - index] == "1" \
                        else len(matrix[0]) - index - 1

        for i in range(1, len(matrix)):
            r, l = len(matrix[0]) - 1, 0
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    if j > 0:
                        left[i][j] = max(l, left[i - 1][j])
                    height[i][j] = height[i - 1][j] + 1
                else:
                    l = j + 1

                if matrix[i][-j - 1] == "1":
                    if j == 0:
                        right[i][-j - 1] = len(matrix[0]) - 1
                    else:
                        right[i][-j - 1] = min(right[i - 1][-j - 1], r)
                else:
                    right[i][-j - 1] = len(matrix[0])
                    r = len(matrix[0]) - j - 2

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, (right[i][j] - left[i][j] + 1) * height[i][j])

        return res


s = Solution()
m = [["1", "0", "1", "0", "0"],
     ["1", "0", "1", "1", "1"],
     ["1", "1", "1", "1", "1"],
     ["1", "0", "0", "1", "0"]]
m = [["0", "1", "1", "0", "0", "1", "0", "1", "0", "1"],
     ["0", "0", "1", "0", "1", "0", "1", "0", "1", "0"],
     ["1", "0", "0", "0", "0", "1", "0", "1", "1", "0"],
     ["0", "1", "1", "1", "1", "1", "1", "0", "1", "0"],
     ["0", "0", "1", "1", "1", "1", "1", "1", "1", "0"],
     ["1", "1", "0", "1", "0", "1", "1", "1", "1", "0"],
     ["0", "0", "0", "1", "1", "0", "0", "0", "1", "0"],
     ["1", "1", "0", "1", "1", "0", "0", "1", "1", "1"],
     ["0", "1", "0", "1", "1", "0", "1", "0", "1", "1"]]
print(s.maximalRectangle(m))


"""
https://leetcode.com/problems/maximal-rectangle/discuss/29054/Share-my-DP-solution/175299
https://leetcode.com/problems/maximal-rectangle/discuss/29054/Share-my-DP-solution/175344

class Solution {
    public int maximalRectangle(char[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0] == null || matrix[0].length == 0) return 0;
        int m = matrix.length, n = matrix[0].length, maxArea = 0;
        int[] left = new int[n];
        int[] right = new int[n];
        int[] height = new int[n];
        Arrays.fill(right, n - 1);
        for (int i = 0; i < m; i++) {
            int rB = n - 1;
            for (int j = n - 1; j >= 0; j--) {
                if (matrix[i][j] == '1') {
                    right[j] = Math.min(right[j], rB);
                } else {
                    right[j] = n - 1;
                    rB = j - 1;
                }
            }
            int lB = 0;
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == '1') {
                    left[j] = Math.max(left[j], lB);
                    height[j]++;
                    maxArea = Math.max(maxArea, height[j] * (right[j] - left[j] + 1));
                } else {
                    height[j] = 0;
                    left[j] = 0;
                    lB = j + 1;
                }
            }
        }
        return maxArea;
    }
}
"""