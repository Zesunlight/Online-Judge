# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 面试题04. 二维数组中的查找
Website: https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 52 ms, 在所有 Python3 提交中击败了48.19%的用户
Memory Usage: 17.8 MB, 在所有 Python3 提交中击败了100.00%的用户
=================================================="""


class Solution:
    """
    在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
    """
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        if m == 1:
            res, _, _ = self.half_search(matrix[0], target)
            return res
        if n == 1:
            res, _, _ = self.half_search([matrix[i][0] for i in range(m)], target)
            return res

        dia = [matrix[i][i] for i in range(min(m, n))]
        bingo, left, right = self.half_search(dia, target)
        if bingo:
            return True
        else:
            if right > min(m, n):
                pass
            else:
                possible = [[matrix[i][j] for j in range(right, n)] for i in range(0, left + 1)]
                maybe = [[matrix[i][j] for j in range(0, right)] for i in range(left + 1, m)]
                return self.findNumberIn2DArray(possible, target) or self.findNumberIn2DArray(maybe, target)

    def half_search(self, vector, n):
        if not vector:
            return False, -1, -1
        if len(vector) == 1:
            if n == vector[0]:
                return True, 0, 0
            elif n < vector[0]:
                return False, -1, 0
        left, right = 0, len(vector) - 1
        middle = (left + right) // 2
        while left <= right:
            if n == vector[middle]:
                return True, middle, middle
            elif n < vector[middle]:
                right = middle - 1
            else:
                left = middle + 1
            middle = (left + right) // 2
        else:
            return False, right, left


"""
我的想法
沿主对角线查找，找到离 target 最近的两个点（一大一小），不妨设为 m,M
依据这两个点把矩阵分为四个部分，左上全部小于m，右下全部大于M
剩下两块再递归
中间用二分辅助计算
"""

"""
从二维数组的右上角开始查找。如果当前元素等于目标值，则返回 true。如果当前元素大于目标值，则移到左边一列。如果当前元素小于目标值，则移到下边一行。

每一次比较都能排除一行或者一列元素

class Solution {
    public boolean findNumberIn2DArray(int[][] matrix, int target) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return false;
        }
        int rows = matrix.length, columns = matrix[0].length;
        int row = 0, column = columns - 1;
        while (row < rows && column >= 0) {
            int num = matrix[row][column];
            if (num == target) {
                return true;
            } else if (num > target) {
                column--;
            } else {
                row++;
            }
        }
        return false;
    }
}

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/solution/mian-shi-ti-04-er-wei-shu-zu-zhong-de-cha-zhao-b-3/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/solution/mian-shi-ti-04-er-wei-shu-zu-zhong-de-cha-zhao-zuo/
"""

"""
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if target in matrix[i]:
                return True
        return False

作者：li-jun-jie-albert
链接：https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/solution/shuang-bai-by-li-jun-jie-albert/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""