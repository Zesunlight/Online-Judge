# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 139. 单词拆分
Website: https://leetcode-cn.com/problems/word-break/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 56 ms, 在所有 Python3 提交中击败了45.96%的用户
Memory Usage: 13.7 MB, 在所有 Python3 提交中击败了16.67%的用户
=================================================="""


class Solution:
    """
    给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，
    判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        res = [False for _ in range(len(s))]
        if s[0] in wordDict:
            res[0] = True
        for i in range(1, len(s)):
            if s[:i+1] in wordDict:
                res[i] = True
                continue
            for j in range(1, i+1):
                if res[j-1] and s[j:i+1] in wordDict:
                    res[i] = True
                    break
        return res[-1]


"""
public class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        Set<String> wordDictSet = new HashSet(wordDict);
        boolean[] dp = new boolean[s.length() + 1];
        dp[0] = true;
        for (int i = 1; i <= s.length(); i++) {
            for (int j = 0; j < i; j++) {
                if (dp[j] && wordDictSet.contains(s.substring(j, i))) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[s.length()];
    }
}

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/word-break/solution/dan-ci-chai-fen-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""