import java.util.*;

/*
    657. 机器人能否返回原点
    https://leetcode-cn.com/problems/robot-return-to-origin/

    在二维平面上，有一个机器人从原点 (0, 0) 开始。给出它的移动顺序，判断这个机器人在完成移动后是否在 (0, 0) 处结束。
    移动顺序由字符串表示。字符 move[i] 表示其第 i 次移动。机器人的有效动作有 R（右），L（左），U（上）和 D（下）。
    如果机器人在完成所有动作后返回原点，则返回 true。否则，返回 false。

    执行用时：18 ms, 在所有 Java 提交中击败了6.24%的用户
    内存消耗：40.4 MB, 在所有 Java 提交中击败了5.02%的用户
 */


class Solution {
    public boolean judgeCircle(String moves) {
        Map<Character, Integer> map = new HashMap<>(){{
            put('R', 0);
            put('L', 0);
            put('U', 0);
            put('D', 0);
        }};
        for (Character c : moves.toCharArray()) {
            map.put(c, map.get(c) + 1);
        }
        if (!map.get('R').equals(map.get('L'))) return false;
        if (!map.get('U').equals(map.get('D'))) return false;
        return true;
    }
}


class Solution2 {
    public boolean judgeCircle(String moves) {
        int x = 0, y = 0;
        int length = moves.length();
        for (int i = 0; i < length; i++) {
            char move = moves.charAt(i);
            if (move == 'U') {
                y--;
            } else if (move == 'D') {
                y++;
            } else if (move == 'L') {
                x--;
            } else if (move == 'R') {
                x++;
            }
        }
        return x == 0 && y == 0;
    }
}

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/robot-return-to-origin/solution/ji-qi-ren-neng-fou-fan-hui-yuan-dian-by-leetcode-s/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。