import java.util.*;

/*
    1025. 除数博弈
    https://leetcode-cn.com/problems/divisor-game/

    爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。

    最初，黑板上有一个数字 N 。在每个玩家的回合，玩家需要执行以下操作：

    选出任一 x，满足 0 < x < N 且 N % x == 0 。
    用 N - x 替换黑板上的数字 N 。
    如果玩家无法执行这些操作，就会输掉游戏。

    只有在爱丽丝在游戏中取得胜利时才返回 True，否则返回 false。假设两个玩家都以最佳状态参与游戏。

    执行用时：3 ms, 在所有 Java 提交中击败了34.30%的用户
    内存消耗：36.7 MB, 在所有 Java 提交中击败了10.00%的用户
 */


class Solution {
    public boolean divisorGame(int N) {
        boolean[] dp = new boolean[N + 1];
        if (N == 1) return false;
        if (N == 2) return true;
        dp[2] = true;
        
        for (int i = 3; i <= N; i++) {
            for (int j = 1; j <= (int)Math.floor(Math.sqrt(i)); j++) {
                if (i % j == 0) {
                    if (!dp[i - j]) {
                        dp[i] = true;
                        break;
                    }
                }
            }
        }

        return dp[N];
    }

    // return N % 2 == 0;
}
