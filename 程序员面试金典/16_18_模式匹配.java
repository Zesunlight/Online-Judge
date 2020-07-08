import java.util.*;

/*
    面试题 16.18. 模式匹配
    https://leetcode-cn.com/problems/pattern-matching-lcci/

    你有两个字符串，即pattern和value。 pattern字符串由字母"a"和"b"组成，用于描述字符串中的模式。
    例如，字符串"catcatgocatgo"匹配模式"aabab"（其中"cat"是"a"，"go"是"b"），该字符串也匹配像"a"、"ab"和"b"这样的模式。
    但需注意"a"和"b"不能同时表示相同的字符串。编写一个方法判断value字符串是否匹配pattern字符串。

    执行用时：211 ms, 在所有 Java 提交中击败了5.06%的用户
    内存消耗：40.4 MB, 在所有 Java 提交中击败了100.00%的用户
 */


class Solution {
    public boolean patternMatching(String pattern, String value) {
        for (int i = 0; i < value.length() + 1; ++i) {
            if (pattern.charAt(0) == 'a') {
                if (patternMatching(pattern.substring(1), value.substring(i), value.substring(0, i), "1")) {
                    return true;
                }
            } else {
                if (patternMatching(pattern.substring(1), value.substring(i), "1", value.substring(0, i))) {
                    return true;
                }
            }
        }
        return false;
    }

    public boolean patternMatching(String pattern, String value, String a, String b) {
        if (a.equals(b)) return false;
        if (pattern.length() == 0) return value.length() == 0;

        if (a.equals("1")) {
            if (pattern.charAt(0) == 'b') {
                int len = b.length();
                if (value.length() < len) return false;

                if (value.substring(0, len).equals(b)) {
                    return patternMatching(pattern.substring(1), value.substring(len), a, b);
                } else {
                    return false;
                }
            } else {
                for (int i = 0; i < value.length() + 1; ++i) {
                    if (patternMatching(pattern.substring(1), value.substring(i), value.substring(0, i), b)) {
                        return true;
                    }
                }
                return false;
            }
        } else if (b.equals("1")) {
            if (pattern.charAt(0) == 'a') {
                int len = a.length();
                if (value.length() < len) return false;

                if (value.substring(0, len).equals(a)) {
                    return patternMatching(pattern.substring(1), value.substring(len), a, b);
                } else {
                    return false;
                }
            } else {
                for (int i = 0; i < value.length() + 1; ++i) {
                    if (patternMatching(pattern.substring(1), value.substring(i), a, value.substring(0, i))) {
                        return true;
                    }
                }
                return false;
            }
        } else {
            if (pattern.charAt(0) == 'a') {
                int len = a.length();
                if (value.length() < len) return false;

                if (value.substring(0, len).equals(a)) {
                    return patternMatching(pattern.substring(1), value.substring(len), a, b);
                } else {
                    return false;
                }
            } else {
                int len = b.length();
                if (value.length() < len) return false;

                if (value.substring(0, len).equals(b)) {
                    return patternMatching(pattern.substring(1), value.substring(len), a, b);
                } else {
                    return false;
                }
            }
        }
    }
}

/*
class Solution {
public:
    int cnt[2];
    bool patternMatching(string pattern, string value) {
        // 分情况讨论
        // 1. pattern为空
        if (pattern.empty()) return value.empty();
        // 2. pattern不为空
        // 2.1 value为空, 判断pattern是否只由一个字母组成
        if (value.empty()) {
            int i = 0;
            while (i < pattern.size() && pattern[i] == pattern[0]) i ++;
            return i == pattern.size();
        }
        // 2.2 pattern不为空，value不为空
        int n = pattern.size(), m = value.size();
        //   预处理统计a, b字母个数cnt[0], cnt[1]
        cnt[0] = cnt[1] = 0;
        for (auto x: pattern) cnt[x - 'a'] ++;
        //   判断cnt[0], cnt[1]是否有为0的情况
        if (!cnt[0]) return helper(value, cnt[1]);
        else if (!cnt[1]) return helper(value, cnt[0]);

        //  2.2.1 假设使得a,b其中之一为空, 即次数为0
        if (helper(value, cnt[0])) return true;
        if (helper(value, cnt[1])) return true;

        // 2.2.2 a,b都不为空; 枚举a, b匹配的长度，使得a * len_a + b * len_b = m; len_a唯一确定len_b，只需枚举len_a
        for (int len_a = 1; len_a * cnt[0] <= m - cnt[1]; len_a ++) {
            if ((m - len_a * cnt[0]) % cnt[1] != 0) continue;
            int len_b = (m - len_a * cnt[0]) / cnt[1];
            if (check(pattern, value, len_a, len_b)) return true;
        }
        return false;
    }

    bool helper(string value, int k) { // pattern不为空，value不为空. 判断是否可以k次切分value
        int m = value.size();
        if (m % k != 0) return false;
        int len = m / k;
        for (int i = len; i < m; i += len)
            if (value.substr(i, len) != value.substr(0, len)) return false;
        return true;
    }

    bool check(string pattern, string value, int len_a, int len_b) { 
        string ps[2] = {"", ""}; // a, b匹配的字符串
        for (int i = 0, j = 0; i < pattern.size(); i ++) { // i, j指针都是恰当长度的
            if (pattern[i] == 'a') {
                if (ps[0] == "") ps[0] = value.substr(j, len_a);
                else if (value.substr(j, len_a) != ps[0]) return false;
                j += len_a;
            } else if (pattern[i] == 'b') {
                if (ps[1] == "") ps[1] = value.substr(j, len_b);
                else if (value.substr(j, len_b) != ps[1]) return false;
                j += len_b;
            }
        }
        return ps[0] != ps[1]; // a,b所匹配的字符串不能相同（这里之前忘了考虑，多谢@重剑（ Rage Your Dream）指出）
    }
};

作者：joswxe
链接：https://leetcode-cn.com/problems/pattern-matching-lcci/solution/shuang-bai-suan-fa-guan-jian-zhao-dao-fen-lei-de-j/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
*/