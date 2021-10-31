import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/*
    500. 键盘行
    https://leetcode-cn.com/problems/keyboard-row/

    给你一个字符串数组 words ，只返回可以使用在 美式键盘 同一行的字母打印出来的单词。键盘如下图所示。

    美式键盘 中：
    第一行由字符 "qwertyuiop" 组成。
    第二行由字符 "asdfghjkl" 组成。
    第三行由字符 "zxcvbnm" 组成。

    执行用时：1 ms
    内存消耗：36.1 MB
 */

class Solution {
    public String[] findWords(String[] words) {
        Set<Character> one = insert("qwertyuiop");
        Set<Character> two = insert("asdfghjkl");
        Set<Character> three = insert("zxcvbnm");

        List<String> result = new ArrayList<>();
        for (String word : words) {
            if (same(word, one) || same(word, two) || same(word, three)) {
                result.add(word);
            }
        }
        return result.toArray(new String[result.size()]);
    }

    public boolean same(String str, Set<Character> set) {
        for (char c : str.toLowerCase().toCharArray()) {
            if (!set.contains(c)) {
                return false;
            }
        }
        return true; 
    }

    public Set<Character> insert(String str) {
        Set<Character> set = new HashSet<>();
        for (char c : str.toCharArray()) {
            set.add(c);
        } 
        return set;
    }
     
    public String[] findWords2(String[] words) {
        // https://leetcode-cn.com/problems/keyboard-row/solution/jian-pan-xing-by-leetcode-solution-bj5e/
        List<String> list = new ArrayList<String>();
        String rowIdx = "12210111011122000010020202";
        for (String word : words) {
            boolean isValid = true;
            char idx = rowIdx.charAt(Character.toLowerCase(word.charAt(0)) - 'a');
            for (int i = 1; i < word.length(); ++i) {
                if (rowIdx.charAt(Character.toLowerCase(word.charAt(i)) - 'a') != idx) {
                    isValid = false;
                    break;
                }
            }
            if (isValid) {
                list.add(word);
            }
        }
        String[] ans = new String[list.size()];
        for (int i = 0; i < list.size(); ++i) {
            ans[i] = list.get(i);
        }
        return ans;
    }

}
