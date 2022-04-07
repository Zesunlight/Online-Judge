/*
    796. 旋转字符串
    https://leetcode-cn.com/problems/rotate-string/submissions/

    给定两个字符串, s和goal。如果在若干次旋转操作之后，s能变成goal，那么返回true。
    s的 旋转操作 就是将s 最左边的字符移动到最右边。
    例如, 若s = 'abcde'，在旋转一次之后结果就是'bcdea'。

    执行用时：0 ms
    内存消耗：39.3 MB
*/

class Solution {
    public boolean rotateString(String s, String goal) {
        if (s.length() != goal.length()) {
            return false;
        }
        int n = s.length();
        for (int i = 0; i < n; i++) {
            boolean flag = true;
            for (int j = 0; j < n; j++) {
                if (s.charAt(j) != goal.charAt((i + j) % n)) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                return true;
            }
        }
        return false;
    }
}

class Solution2 {
    public boolean rotateString(String s, String goal) {
        return s.length() == goal.length() && (s + s).contains(goal);
    }
    // 作者：LeetCode-Solution
    // 链接：https://leetcode-cn.com/problems/rotate-string/solution/xuan-zhuan-zi-fu-chuan-by-leetcode-solut-4hlp/
    // 来源：力扣（LeetCode）
    // 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
}

