# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 面试题64. 求1+2+…+n
Website: https://leetcode-cn.com/problems/qiu-12n-lcof/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 32 ms, 在所有 Python3 提交中击败了98.29%的用户
Memory Usage: 13.6 MB, 在所有 Python3 提交中击败了100.00%的用户
=================================================="""


class Solution:
    """
    求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
    """
    def sumNums(self, n: int) -> int:
        import math
        return (int(math.exp(math.log(n) + math.log(n)) + 0.5) + n) >> 1

"""
逻辑运算符的短路效应

if(A && B)  // 若 A 为 false ，则 B 的判断不会执行（即短路），直接判定 A && B 为 false

if(A || B) // 若 A 为 true ，则 B 的判断不会执行（即短路），直接判定 A || B 为 true
"""

"""
快速乘 「俄罗斯农民乘法」
int quickMulti(int A, int B) {
    int ans = 0;
    for ( ; B; B >>= 1) {
        if (B & 1) {
            ans += A;
        }
        A <<= 1;
    }
    return ans;
}

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/qiu-12n-lcof/solution/qiu-12n-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
