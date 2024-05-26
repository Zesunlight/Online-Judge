import java.util.*;

/*
    30. 串联所有单词的子串
    https://leetcode.cn/problems/substring-with-concatenation-of-all-words/description/

    给定一个字符串 s 和一个字符串数组 words。 words 中所有字符串 长度相同。
     s 中的 串联子串 是指一个包含  words 中所有字符串以任意顺序排列连接起来的子串。

    例如，如果 words = ["ab","cd","ef"]， 那么 "abcdef"， "abefcd"，"cdabef"， "cdefab"，"efabcd"， 和 "efcdab" 都是串联子串。
    "acdbef" 不是串联子串，因为他不是任何 words 排列的连接。
    返回所有串联子串在 s 中的开始索引。你可以以 任意顺序 返回答案。

    执行用时：2192 ms, 在所有 Java 提交中击败了10.11%的用户
    内存消耗：44.96 MB, 在所有 Java 提交中击败了27.11%的用户
 */
class Solution {

    public List<Integer> findSubstring(String s, String[] words) {
        int l = words[0].length();
        int n = words.length;
        if (s.length() < n * l) {
            return new ArrayList<>();
        }

        Map<String, Integer> dict = new HashMap<>();
        for (String w : words) {
            int c = dict.getOrDefault(w, 0);
            dict.put(w, c + 1);
        }

        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < s.length() - l * n + 1; i++) {
            Map<String, Integer> temp = new HashMap<>();
            int j = 0;
            for (; j < n; j++) {
                String word = s.substring(i + j * l, i + (j + 1) * l);
                if (!dict.containsKey(word)) {
                    break;
                } else {
                    int c = temp.getOrDefault(word, 0);
                    temp.put(word, c + 1);
                    if (dict.get(word) < temp.get(word)) {
                        break;
                    }
                }
            }

            if (j == n) {
                result.add(i);
            }
        }

        return result;
    }
}

public class LeetCode {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.findSubstring("barfoofoobarthefoobarman", new String[]{"foo","bar", "the"}));
    }
}
