/*
    520. 检测大写字母
    https://leetcode-cn.com/problems/detect-capital/submissions/

    我们定义，在以下情况时，单词的大写用法是正确的：
    全部字母都是大写，比如 "USA" 。
    单词中所有字母都不是大写，比如 "leetcode" 。
    如果单词不只含有一个字母，只有首字母大写， 比如 "Google" 。
    给你一个字符串 word 。如果大写用法正确，返回 true ；否则，返回 false 。

    执行用时：1 ms
    内存消耗：36.7 MB
 */

class Solution {
    public boolean detectCapitalUse(String word) {
        if (Character.isLowerCase(word.charAt(0))) {
            for (Character c : word.toCharArray()) {
                if (Character.isUpperCase(c)) {
                    return false;
                }
            }
        } else {
            int n = word.length();
            if (n >= 2) {
                if (Character.isLowerCase(word.charAt(1))) {
                    for (int i = 2; i < n; i++) {
                        if (Character.isUpperCase(word.charAt(i))) {
                            return false;
                        }
                    }
                } else {
                    for (int i = 2; i < n; i++) {
                        if (Character.isLowerCase(word.charAt(i))) {
                            return false;
                        }
                    }
                }
            }
        }
        return true;
    }

    public boolean detectCapitalUse2(String word) {
        // https://leetcode-cn.com/problems/detect-capital/solution/jian-ce-da-xie-zi-mu-by-leetcode-solutio-449z/
        // 若第 1 个字母为小写，则需额外判断第 2 个字母是否为小写
        if (word.length() >= 2 && Character.isLowerCase(word.charAt(0)) && Character.isUpperCase(word.charAt(1))) {
            return false;
        }
        
        // 无论第 1 个字母是否大写，其他字母必须与第 2 个字母的大小写相同
        for (int i = 2; i < word.length(); ++i) {
            if (Character.isLowerCase(word.charAt(i)) ^ Character.isLowerCase(word.charAt(1))) {
                return false;
            }
        }
        return true;
    }

    public boolean detectCapitalUse3(String word) {
        // https://leetcode-cn.com/problems/detect-capital/solution/jian-ce-da-xie-zi-mu-by-leetcode-solutio-449z/1226717
        return word.equals(word.toUpperCase()) || word.substring(1).equals(word.substring(1).toLowerCase());
    }

}
public class LeetCode {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.detectCapitalUse("G"));
    }
}
