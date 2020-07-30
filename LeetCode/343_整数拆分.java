import java.util.*;

/*
    343. 整数拆分
    https://leetcode-cn.com/problems/integer-break/

    给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

    执行用时：0 ms, 在所有 Java 提交中击败了100.00%的用户
    内存消耗：36.4 MB, 在所有 Java 提交中击败了40.82%的用户
 */


class Solution {
    public int integerBreak(int n) {
        if (n <= 3) return n - 1;
        int d = n / 3;
        int r = n % 3;
        if (r == 0) return (int)Math.pow(3, d);
        if (r == 1) return (int)Math.pow(3, d - 1) * 4;
        return (int)Math.pow(3, d) * 2;
    }
}


class Solution2 {
    public int integerBreak(int n) {
        if (n < 4) {
            return n - 1;
        }
        int[] dp = new int[n + 1];
        dp[2] = 1;
        for (int i = 3; i <= n; i++) {
            dp[i] = Math.max(Math.max(2 * (i - 2), 2 * dp[i - 2]), Math.max(3 * (i - 3), 3 * dp[i - 3]));
        }
        return dp[n];
    }
}

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/integer-break/solution/zheng-shu-chai-fen-by-leetcode-solution/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
