# -*- coding: UTF-8 -*-
"""
=================================================
Problem: 5740. 所有元音按顺序排布的最长子字符串
Website: https://leetcode-cn.com/problems/longest-substring-of-all-vowels-in-order/
Difficulty: 中等
Author: ZYZ
Language: Python3
Result: Accepted
Runtime: 508 ms
Memory Usage: 17.1 MB
=================================================="""


class Solution:
    """
    当一个字符串满足如下条件时，我们称它是 美丽的 ：

    所有 5 个英文元音字母（'a' ，'e' ，'i' ，'o' ，'u'）都必须 至少 出现一次。
    这些元音字母的顺序都必须按照 字典序 升序排布（也就是说所有的 'a' 都在 'e' 前面，所有的 'e' 都在 'i' 前面，以此类推）
    比方说，字符串 "aeiou" 和 "aaaaaaeiiiioou" 都是 美丽的 ，但是 "uaeio" ，"aeoiu" 和 "aaaeeeooo" 不是美丽的 。

    给你一个只包含英文元音字母的字符串 word ，请你返回 word 中 最长美丽子字符串的长度 。如果不存在这样的子字符串，请返回 0 。

    子字符串 是字符串中一个连续的字符序列。
    """

    def longestBeautifulSubstring(self, word: str) -> int:
        state = 0
        m = 0
        ans = 0

        for w in word:
            if state == 0:
                if w == 'a':
                    m += 1
                    state = 1
                else:
                    m = 0
            elif state == 1:
                if w == 'e':
                    m += 1
                    state = 2
                elif w == 'a':
                    m += 1
                else:
                    m = 0
                    state = 0
            elif state == 2:
                if w == 'i':
                    m += 1
                    state = 3
                elif w == 'e':
                    m += 1
                elif w == 'a':
                    m = 1
                    state = 0
                else:
                    m = 0
                    state = 0
            elif state == 3:
                if w == 'o':
                    m += 1
                    state = 4
                elif w == 'i':
                    m += 1
                elif w == 'a':
                    m = 1
                    state = 0
                else:
                    m = 0
                    state = 0
            elif state == 4:
                if w == 'u':
                    m += 1
                    ans = max(ans, m)
                    state = 5
                elif w == 'o':
                    m += 1
                elif w == 'a':
                    m = 1
                    state = 0
                else:
                    m = 0
                    state = 0
            elif state == 5:
                if w == 'u':
                    m += 1
                    ans = max(ans, m)
                elif w == 'a':
                    m = 1
                    state = 0
                else:
                    m = 0
                    state = 0

        return ans


    TRANSIT = {
        ("a", "e"), ("e", "i"), ("i", "o"), ("o", "u"),
        ("a", "a"), ("e", "e"), ("i", "i"), ("o", "o"), ("u", "u"),
        ("x", "a"), ("e", "a"), ("i", "a"), ("o", "a"), ("u", "a"),
    }
    
    def longestBeautifulSubstring(self, word: str) -> int:
        cur, ans = 0, 0
        status = "x"
        
        for ch in word:
            if (status, ch) in Solution.TRANSIT:
                if status != "a" and ch == "a":
                    cur = 1
                else:
                    cur = cur + 1
                status = ch
            else:
                cur = 0
                status = "x"
            if status == "u":
                ans = max(ans, cur)

        return ans

    # 作者：LeetCode-Solution
    # 链接：https://leetcode-cn.com/problems/longest-substring-of-all-vowels-in-order/solution/suo-you-yuan-yin-an-shun-xu-pai-bu-de-zu-9wqg/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


"""
class Solution {
public:
    int longestBeautifulSubstring(string word) {
        if (word.size()<5)return 0;
        int res=0;
        int rlen=1;
        int vowel=1;
        for(int i=1;i<word.length();i++){
            if(word[i]>=word[i-1])rlen++;
            if(word[i]>word[i-1])vowel++;
            if(word[i]<word[i-1]){rlen=1;vowel=1;}
            if(vowel==5){res=rlen>res?rlen:res;}
        }
        return res;
    }
};

作者：SweetpepperJ
链接：https://leetcode-cn.com/problems/longest-substring-of-all-vowels-in-order/solution/bi-da-xiao-by-sweetpepperj-gdlt/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
