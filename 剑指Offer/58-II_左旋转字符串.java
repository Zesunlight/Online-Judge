/*
=================================================
Problem: 面试题 58 - II. 左旋转字符串
Website: https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/
Difficulty: 简单
Author: ZYZ
Language: Java
Result: Accepted
Runtime: 0 ms, 在所有 Python3 提交中击败了100.00%的用户
Memory Usage: 39.8 MB, 在所有 Python3 提交中击败了100.00%的用户
==================================================*/


class Solution {
    public String reverseLeftWords(String s, int n) {
        return s.substring(n) + s.substring(0, n);
    }
}

class Solution2 {
    public String reverseLeftWords(String s, int n) {
        StringBuilder res = new StringBuilder();
        for(int i = n; i < n + s.length(); i++)
            res.append(s.charAt(i % s.length()));
        return res.toString();
    }
}

class Solution3 {
    public String reverseLeftWords(String s, int n) {
        String res = "";
        for(int i = n; i < s.length(); i++)
            res += s.charAt(i);
        for(int i = 0; i < n; i++)
            res += s.charAt(i);
        return res;
    }
}

// 作者：jyd
// 链接：https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/solution/mian-shi-ti-58-ii-zuo-xuan-zhuan-zi-fu-chuan-qie-p/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。