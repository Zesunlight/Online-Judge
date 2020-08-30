import java.util.*;

/*
    557. 反转字符串中的单词 III
    https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/

    给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

    执行用时：21 ms, 在所有 Java 提交中击败了19.54%的用户
    内存消耗：41 MB, 在所有 Java 提交中击败了6.33%的用户
 */


class Solution {
    public String reverseWords(String s) {
        StringBuilder r = new StringBuilder(), t = new StringBuilder();
        for (Character c : s.toCharArray()) {
            if (c == ' ') {
                r.append(t.reverse().append(c));
                t = new StringBuilder();
            } else {
                t.append(c);
            }
        }
        r.append(t.reverse());
        return r.toString();
    }
}


/*

return ' '.join(s.split(' ')[::-1])[::-1]

return ' '.join([word[::-1] for word in s.split(' ')])

*/