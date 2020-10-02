import java.util.*;

/*
    771. 宝石与石头
    https://leetcode-cn.com/problems/jewels-and-stones/

    给定字符串J 代表石头中宝石的类型，和字符串 S代表你拥有的石头。 
    S 中每个字符代表了一种你拥有的石头的类型，你想知道你拥有的石头中有多少是宝石。
    J 中的字母不重复，J 和 S中的所有字符都是字母。字母区分大小写，因此"a"和"A"是不同类型的石头。

    执行用时：1 ms, 在所有 Java 提交中击败了99.67%的用户
    内存消耗：37.2 MB, 在所有 Java 提交中击败了54.84%的用户
 */


class Solution {
    public int numJewelsInStones(String J, String S) {
        int jade = 0;
        for (int i = 0; i < J.length(); i++) {
            for (int j = 0; j < S.length(); j++) {
                if (J.charAt(i) == S.charAt(j)) jade++;
            }
        }
        return jade;
    }
}


class Solution2 {
    public int numJewelsInStones(String J, String S) {
        int jewelsCount = 0;
        Set<Character> jewelsSet = new HashSet<Character>();
        int jewelsLength = J.length(), stonesLength = S.length();
        for (int i = 0; i < jewelsLength; i++) {
            char jewel = J.charAt(i);
            jewelsSet.add(jewel);
        }
        for (int i = 0; i < stonesLength; i++) {
            char stone = S.charAt(i);
            if (jewelsSet.contains(stone)) {
                jewelsCount++;
            }
        }
        return jewelsCount;
    }
}

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/jewels-and-stones/solution/bao-shi-yu-shi-tou-by-leetcode-solution/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。