/*
    2562. 找出数组的串联值
    https://leetcode.cn/problems/minimum-window-substring/

    给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。
    如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

    对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
    如果 s 中存在这样的子串，我们保证它是唯一的答案。

    执行用时：99 ms
    内存消耗：42.9 MB
 */


class Solution {
    public String minWindow(String s, String t) {
        if (s == null || s.isEmpty() || t == null || t.isEmpty() || s.length() < t.length()) {
            return "";
        }

        Map<Character, Integer> counter = new HashMap<>();
        for (int i = 0; i < t.length(); i++) {
            counter.put(t.charAt(i), counter.getOrDefault(t.charAt(i), 0) + 1);
        }
        int need = t.length();
        int start = 0;
        int end = 0;
        boolean match = false;
        String result = s;
        while (end < s.length()) {
            if (counter.containsKey(s.charAt(end))) {
                counter.put(s.charAt(end), counter.get(s.charAt(end)) - 1);
                if (counter.get(s.charAt(end)) >= 0) {
                    need--;
                }
            }

            while (need == 0) {
                match = true;
                if ((end - start + 1) < result.length()) {
                    result = s.substring(start, end + 1);
                }
                if (counter.containsKey(s.charAt(start))) {
                    counter.put(s.charAt(start), counter.get(s.charAt(start)) + 1);
                    if (counter.get(s.charAt(start)) > 0) {
                        need++;
                    }
                }

                start++;
            }

            end++;
        }

        return match ? result : "";
    }
}


public class LeetCode {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.minWindow("aab", "ab"));
    }
}
