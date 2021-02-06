# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 58. 最后一个单词的长度
Website: https://leetcode-cn.com/problems/length-of-last-word/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 40 ms
Memory Usage: 14.7 MB
=================================================="""


class Solution:
    """
    给你一个字符串 s，由若干单词组成，单词之间用空格隔开。返回字符串中最后一个单词的长度。如果不存在最后一个单词，请返回 0 。
    单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。
    """
    def lengthOfLastWord(self, s: str) -> int:
        w = s.strip().split()
        if w:
            return len(w[-1])
        else:
            return 0

"""
class Solution {
    public int lengthOfLastWord(String s) {
        int end = s.length() - 1;
        while(end >= 0 && s.charAt(end) == ' ') end--;
        if(end < 0) return 0;
        int start = end;
        while(start >= 0 && s.charAt(start) != ' ') start--;
        return end - start;
    }
}

作者：guanpengchn
链接：https://leetcode-cn.com/problems/length-of-last-word/solution/hua-jie-suan-fa-58-zui-hou-yi-ge-dan-ci-de-chang-d/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""