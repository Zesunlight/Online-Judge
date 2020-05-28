# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 14. 最长公共前缀
Website: https://leetcode-cn.com/problems/longest-common-prefix/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 44 ms, 在所有 Python3 提交中击败了59.04%的用户
Memory Usage: 13.7 MB, 在所有 Python3 提交中击败了6.15%的用户
=================================================="""


class Solution:
    """
    编写一个函数来查找字符串数组中的最长公共前缀。

    如果不存在公共前缀，返回空字符串 ""。
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs is None or len(strs) == 0:
            return ''
        left = min(strs)
        right = max(strs)
        res = ''
        for i in range(min(len(left), len(right))):
            if left[i] == right[i]:
                res += left[i]
            else:
                break
        return res


"""
https://leetcode-cn.com/problems/longest-common-prefix/comments/38495
def longestCommonPrefix(self, strs):
    if not strs: return ""
    ss = list(map(set, zip(*strs)))
    res = ""
    for i, x in enumerate(ss):
        x = list(x)
        if len(x) > 1:
            break
        res = res + x[0]
    return res

https://leetcode-cn.com/problems/longest-common-prefix/solution/zui-chang-gong-gong-qian-zhui-by-leetcode/
查找一组字符串的最长公共前缀 LCP(S_1 ldots S_n)的简单方法。我们将会用到这样的结论：

LCP(S_1 ldots S_n) = LCP(LCP(LCP(S_1, S_2),S_3),ldots S_n)
"""