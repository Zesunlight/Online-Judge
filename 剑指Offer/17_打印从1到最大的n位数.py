# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 面试题17. 打印从1到最大的n位数
Website: https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 36 ms, 在所有 Python3 提交中击败了96.38%的用户
Memory Usage: 19.1 MB, 在所有 Python3 提交中击败了100.00%的用户
=================================================="""


class Solution:
    """
    输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。
    比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。
    """
    def printNumbers(self, n: int) -> List[int]:
        return [i for i in range(1, int('1' + '0' * n))]

"""
class Solution:
    def printNumbers(self, n: int) -> List[int]:
        return list(range(1, 10 ** n))

作者：jyd
链接：https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/solution/mian-shi-ti-17-da-yin-cong-1-dao-zui-da-de-n-wei-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
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
