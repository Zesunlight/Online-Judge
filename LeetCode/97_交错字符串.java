/*
    97. 交错字符串
    https://leetcode-cn.com/problems/interleaving-string/

    给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。

    执行用时：9 ms, 在所有 Java 提交中击败了25.29%的用户
    内存消耗：38.4 MB, 在所有 Java 提交中击败了14.29%的用户
 */


class Solution {
    public boolean isInterleave(String s1, String s2, String s3) {
        if (s1.equals("")) return s2.equals(s3);
        if (s2.equals("")) return s1.equals(s3);
        if (s3.length() != (s1.length() + s2.length())) return false;

        boolean[][] res = new boolean[s1.length() + 1][s2.length() + 1];
        for (int i = 0; i <= s2.length(); ++i) {
            res[0][i] = s2.substring(0, i).equals(s3.substring(0, i));
        }
        for (int i = 0; i <= s1.length(); ++i) {
            res[i][0] = s1.substring(0, i).equals(s3.substring(0, i));
        }

        for (int i = 1; i <= s1.length(); ++i) {
            for (int j = 1; j <= s2.length(); ++j) {
                boolean temp = false;
                if (s1.charAt(i - 1) == s3.charAt(i + j - 1)) temp = res[i - 1][j];
                if (s2.charAt(j - 1) == s3.charAt(i + j - 1)) temp = res[i][j - 1] || temp;
                res[i][j] = temp;
            }
        }

        return res[s1.length()][s2.length()];
    }
}

class Solution2 {
    public boolean isInterleave(String s1, String s2, String s3) {
        int n = s1.length(), m = s2.length(), t = s3.length();

        if (n + m != t) {
            return false;
        }

        boolean[][] f = new boolean[n + 1][m + 1];

        f[0][0] = true;
        for (int i = 0; i <= n; ++i) {
            for (int j = 0; j <= m; ++j) {
                int p = i + j - 1;
                if (i > 0) {
                    f[i][j] = f[i][j] || (f[i - 1][j] && s1.charAt(i - 1) == s3.charAt(p));
                }
                if (j > 0) {
                    f[i][j] = f[i][j] || (f[i][j - 1] && s2.charAt(j - 1) == s3.charAt(p));
                }
            }
        }

        return f[n][m];
    }
}

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/interleaving-string/solution/jiao-cuo-zi-fu-chuan-by-leetcode-solution/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution3 {
    public boolean isInterleave(String s1, String s2, String s3) {
        int n = s1.length(), m = s2.length(), t = s3.length();

        if (n + m != t) {
            return false;
        }

        boolean[] f = new boolean[m + 1];

        f[0] = true;
        for (int i = 0; i <= n; ++i) {
            for (int j = 0; j <= m; ++j) {
                int p = i + j - 1;
                if (i > 0) {
                    f[j] = f[j] && s1.charAt(i - 1) == s3.charAt(p);
                }
                if (j > 0) {
                    f[j] = f[j] || (f[j - 1] && s2.charAt(j - 1) == s3.charAt(p));
                }
            }
        }

        return f[m];
    }
}

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/interleaving-string/solution/jiao-cuo-zi-fu-chuan-by-leetcode-solution/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。