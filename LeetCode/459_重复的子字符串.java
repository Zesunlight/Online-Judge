import java.util.*;

/*
    459. 重复的子字符串
    https://leetcode-cn.com/problems/repeated-substring-pattern/

    给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。
    给定的字符串只含有小写英文字母，并且长度不超过10000。

    执行用时：8 ms, 在所有 Java 提交中击败了92.46%的用户
    内存消耗：40.1 MB, 在所有 Java 提交中击败了70.98%的用户
 */


class Solution {
    public boolean repeatedSubstringPattern(String s) {
        int n = s.length();
        for (int i = 1; i <= n / 2; i++) {
            if (n % i == 0) {
                String repeat = s.substring(0, i);
                boolean match = true;
                for (int j = 1; j < n / i; j++) {
                    if (!s.substring(j * i, (j + 1) * i).equals(repeat)) {
                        match = false;
                        break;
                    }
                }
                if (match) return true;
            }
        }
        return false;
    }
}


class Solution2 {
    public boolean repeatedSubstringPattern(String s) {
        return (s + s).indexOf(s, 1) != s.length();
    }
}

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/repeated-substring-pattern/solution/zhong-fu-de-zi-zi-fu-chuan-by-leetcode-solution/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
