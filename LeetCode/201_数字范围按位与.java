import java.util.*;

/*
    201. 数字范围按位与
    https://leetcode-cn.com/problems/bitwise-and-of-numbers-range/

    给定范围 [m, n]，其中 0 <= m <= n <= 2147483647，
    返回此范围内所有数字的按位与（包含 m, n 两端点）。

    执行用时：6 ms, 在所有 Java 提交中击败了99.82%的用户
    内存消耗：39.2 MB, 在所有 Java 提交中击败了34.55%的用户
 */


class Solution {
    public int rangeBitwiseAnd(int m, int n) {
        int shift = 0;
        while (m != n) {
            m = m >> 1;
            n >>= 1;
            shift++;
        }
        return m << shift;
    }
}


class Solution2 {
    public int rangeBitwiseAnd(int m, int n) {
        while (m < n) {
            // 抹去最右边的 1
            n = n & (n - 1);
        }
        return n;
    }
}

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/bitwise-and-of-numbers-range/solution/shu-zi-fan-wei-an-wei-yu-by-leetcode-solution/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。