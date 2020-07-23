/*
    10. 正则表达式匹配
    https://leetcode-cn.com/problems/regular-expression-matching/

    给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

    执行用时：54 ms, 在所有 Java 提交中击败了25.72%的用户
    内存消耗：40 MB, 在所有 Java 提交中击败了26.47%的用户
 */

import java.util.regex.*;

class Solution {
    public boolean isMatch(String s, String p) {
        return Pattern.matches(p, s);
    }
}
