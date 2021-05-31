import java.util.*;

/*
    342. 4的幂
    https://leetcode-cn.com/problems/power-of-four/

    给定一个整数，写一个函数来判断它是否是 4 的幂次方。如果是，返回 true ；否则，返回 false 。
    整数 n 是 4 的幂次方需满足：存在整数 x 使得 n == 4x

    执行用时：1 ms
    内存消耗：35.4 MB
 */


class Solution {
    public boolean isPowerOfFour(int n) {
        if (n >= 1) {
            while (n != 1) {
                if (n % 4 == 0) {
                    n = n / 4;
                } else {
                    return false;
                }
            }
            return true;
        } else {
            return false;
        }
    }

    public boolean isPowerOfFour2(int n) {
        return n > 0 && (n & (n - 1)) == 0 && (n & 0xaaaaaaaa) == 0;
    }

    public boolean isPowerOfFour3(int n) {
        return n > 0 && (n & (n - 1)) == 0 && n % 3 == 1;
    }

    // 作者：LeetCode-Solution
    // 链接：https://leetcode-cn.com/problems/power-of-four/solution/4de-mi-by-leetcode-solution-b3ya/
    // 来源：力扣（LeetCode）
    // 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
}
