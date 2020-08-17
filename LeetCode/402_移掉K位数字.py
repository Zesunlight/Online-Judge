# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 402. 移掉K位数字
Website: https://leetcode-cn.com/problems/remove-k-digits/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 48 ms, 在所有 Python3 提交中击败了74.39%的用户
Memory Usage: 13.9 MB, 在所有 Python3 提交中击败了23.74%的用户
=================================================="""


class Solution:
    """
    给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小。
    """
    def removeKdigits(self, num: str, k: int) -> str:
        if k == 0:
            return num
        else:
            num += '0'
            res = []

            for c in num:
                while res and res[-1] > c:
                    if k == 0:
                        break
                    res.pop()
                    k -= 1
                res.append(c)

            for i in range(len(res)):
                if res[i] != '0':
                    return ''.join(res[i:-1])
            else:
                return '0'


class Solution2:
    def removeKdigits(self, num: str, k: int) -> str:
        numStack = []
        
        # Construct a monotone increasing sequence of digits
        for digit in num:
            while k and numStack and numStack[-1] > digit:
                numStack.pop()
                k -= 1
        
            numStack.append(digit)
        
        # - Trunk the remaining K digits at the end
        # - in the case k==0: return the entire list
        finalStack = numStack[:-k] if k else numStack
        
        # trip the leading zeros
        return "".join(finalStack).lstrip('0') or "0"

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/remove-k-digits/solution/yi-diao-kwei-shu-zi-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。