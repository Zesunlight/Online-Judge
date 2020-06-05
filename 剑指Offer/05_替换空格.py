# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 面试题05. 替换空格
Website: https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 40 ms, 在所有 Python3 提交中击败了63.79%的用户
Memory Usage: 13.8 MB, 在所有 Python3 提交中击败了100.00%的用户
=================================================="""


class Solution:
    """
    请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
    """
    def replaceSpace(self, s: str) -> str:
        return "%20".join(s.split(' '))

"""
string array;   //存储结果
for(auto &c : s){   //遍历原字符串
    if(c == ' '){
        array += "%20"；
    }
    else{
        array += 'c'；
    }
"""
