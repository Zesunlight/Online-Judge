import java.util.*;

/*
    392. 判断子序列
    https://leetcode-cn.com/problems/is-subsequence/

    给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
    你可以认为 s 和 t 中仅包含英文小写字母。
    字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。
    字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。
    （例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

    执行用时：2 ms, 在所有 Java 提交中击败了47.34%的用户
    内存消耗：37.2 MB, 在所有 Java 提交中击败了100.00%的用户
 */


class Solution {
    public boolean isSubsequence(String s, String t) {
        if (s.equals("")) return true;
        if (t.equals("")) return false;
        
        int i = 0, j = 0;
        while (true) {
            if (s.charAt(i) == t.charAt(j)) ++i;
            ++j;
            if (i == s.length()) return true;
            if (j == t.length()) return false;
        }
    }
}


class Solution2 {
    public boolean isSubsequence(String s, String t) {
        int n = s.length(), m = t.length();
        int i = 0, j = 0;
        while (i < n && j < m) {
            if (s.charAt(i) == t.charAt(j)) {
                i++;
            }
            j++;
        }
        return i == n;
    }
}

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/is-subsequence/solution/pan-duan-zi-xu-lie-by-leetcode-solution/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution3 {
    // 令 f[i][j] 表示字符串 t 中从位置 i 开始往后字符 j 第一次出现的位置。
    // 在进行状态转移时，如果 t 中位置 i 的字符就是 j，那么 f[i][j]=i，
    // 否则 j 出现在位置 i+1 开始往后，即 f[i][j]=f[i+1][j]，因此我们要倒过来进行动态规划，从后往前枚举 i。

    public boolean isSubsequence(String s, String t) {
        int n = s.length(), m = t.length();

        int[][] f = new int[m + 1][26];
        for (int i = 0; i < 26; i++) {
            f[m][i] = m;
        }

        for (int i = m - 1; i >= 0; i--) {
            for (int j = 0; j < 26; j++) {
                if (t.charAt(i) == j + 'a')
                    f[i][j] = i;
                else
                    f[i][j] = f[i + 1][j];
            }
        }
        int add = 0;
        for (int i = 0; i < n; i++) {
            if (f[add][s.charAt(i) - 'a'] == m) {
                return false;
            }
            add = f[add][s.charAt(i) - 'a'] + 1;
        }
        return true;
    }
}

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/is-subsequence/solution/pan-duan-zi-xu-lie-by-leetcode-solution/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。