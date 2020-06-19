# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 面试题50. 第一个只出现一次的字符
Website: https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/
Difficulty: 简单
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 68 ms, 在所有 Python3 提交中击败了99.01%的用户
Memory Usage: 13.6 MB, 在所有 Python3 提交中击败了100.00%的用户
=================================================="""


class Solution:
    """
    在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。
    """
    def firstUniqChar(self, s: str) -> str:
        c = collections.Counter(s)
        for k, v in c.items():
            if v == 1:
                return k
        else:
            return ' '

'''
class Solution {
    public char firstUniqChar(String s) {
        Map<Character, Boolean> dic = new LinkedHashMap<>();
        char[] sc = s.toCharArray();
        for(char c : sc)
            dic.put(c, !dic.containsKey(c));
        for(Map.Entry<Character, Boolean> d : dic.entrySet()){
           if(d.getValue()) return d.getKey();
        }
        return ' ';
    }
}

作者：jyd
链接：https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/solution/mian-shi-ti-50-di-yi-ge-zhi-chu-xian-yi-ci-de-zi-3/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

'''
Map<Character, Boolean> dic = new HashMap<>();

char[] array = s.toCharArray();

for (char c : array) {
    dic.put(c, !dic.containsKey(c));
}

for (char c : array) {
    if (dic.get(c)) return c;
}

return ' ';

https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/solution/mian-shi-ti-50-di-yi-ge-zhi-chu-xian-yi-ci-de-zi-3/316190
'''