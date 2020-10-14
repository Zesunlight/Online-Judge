/*
    1002. 查找常用字符
    https://leetcode-cn.com/problems/find-common-characters/

    给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。
    例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。
    你可以按任意顺序返回答案。

    执行用时：12 ms, 在所有 Java 提交中击败了25.26%的用户
    内存消耗：38.6 MB, 在所有 Java 提交中击败了98.14%的用户
 */


class Solution {
    public List<String> commonChars(String[] A) {
        HashMap<Character, Integer> map = new HashMap<>();
        for (Character c : A[0].toCharArray()) {
            map.put(c, map.getOrDefault(c, 0) + 1);
        }
        for (int i = 1; i < A.length; i++) {
            HashMap<Character, Integer> temp = new HashMap<>();
            for (Character c : A[i].toCharArray()) {
                if (map.containsKey(c)) {
                    temp.put(c, temp.getOrDefault(c, 0) + 1);
                    if (map.get(c) == 1) map.remove(c);
                    else map.put(c, map.get(c) - 1);
                }
            }
            map = temp;
        }
        
        List<String> result = new ArrayList<>();
        for (Character c : map.keySet()) {
            for (int i = 0; i < map.get(c); i++) {
                result.add(c.toString());
            }
        }
        return result;
    }
}


class Solution2 {
    public List<String> commonChars(String[] A) {
        int[] minfreq = new int[26];
        Arrays.fill(minfreq, Integer.MAX_VALUE);
        for (String word: A) {
            int[] freq = new int[26];
            int length = word.length();
            for (int i = 0; i < length; ++i) {
                char ch = word.charAt(i);
                ++freq[ch - 'a'];
            }
            for (int i = 0; i < 26; ++i) {
                minfreq[i] = Math.min(minfreq[i], freq[i]);
            }
        }

        List<String> ans = new ArrayList<String>();
        for (int i = 0; i < 26; ++i) {
            for (int j = 0; j < minfreq[i]; ++j) {
                ans.add(String.valueOf((char) (i + 'a')));
            }
        }
        return ans;
    }
}

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/find-common-characters/solution/cha-zhao-chang-yong-zi-fu-by-leetcode-solution/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。