import java.util.*;

/*
    696. 计数二进制子串
    https://leetcode-cn.com/problems/count-binary-substrings/

    给定一个字符串 s，计算具有相同数量0和1的非空(连续)子字符串的数量，
    并且这些子字符串中的所有0和所有1都是组合在一起的。
    重复出现的子串要计算它们出现的次数。

    执行用时：16 ms, 在所有 Java 提交中击败了24.17%的用户
    内存消耗：40.2 MB, 在所有 Java 提交中击败了57.99%的用户
 */


class Solution {
    public int countBinarySubstrings(String s) {
        int zero = 0, one = 0, ans = 0;
        for (int i = 0; i < s.length() - 1; i++) {
            if (s.charAt(i) == '0') {
                zero++;
                if (zero <= one) ans++;
                if (s.charAt(i + 1) == '1') {
                    one = 0;
                }
            } else {
                one++;
                if (one <= zero) ans++;
                if (s.charAt(i + 1) == '0') {
                    zero = 0;
                }
            }
        }
        if (s.charAt(s.length() - 1) == '0') {
            if (++zero <= one) ans++;
        } else {
            if (++one <= zero) ans++;
        }
        return ans;
    }
}


class Solution2 {
    public int countBinarySubstrings(String s) {
        List<Integer> counts = new ArrayList<Integer>();
        int ptr = 0, n = s.length();
        while (ptr < n) {
            char c = s.charAt(ptr);
            int count = 0;
            while (ptr < n && s.charAt(ptr) == c) {
                ++ptr;
                ++count;
            }
            counts.add(count);
        }
        int ans = 0;
        for (int i = 1; i < counts.size(); ++i) {
            ans += Math.min(counts.get(i), counts.get(i - 1));
        }
        return ans;
    }
}

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/count-binary-substrings/solution/ji-shu-er-jin-zhi-zi-chuan-by-leetcode-solution/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution3 {
    public int countBinarySubstrings(String s) {
        int ptr = 0, n = s.length(), last = 0, ans = 0;
        while (ptr < n) {
            char c = s.charAt(ptr);
            int count = 0;
            while (ptr < n && s.charAt(ptr) == c) {
                ++ptr;
                ++count;
            }
            ans += Math.min(count, last);
            last = count;
        }
        return ans;
    }
}

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/count-binary-substrings/solution/ji-shu-er-jin-zhi-zi-chuan-by-leetcode-solution/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。