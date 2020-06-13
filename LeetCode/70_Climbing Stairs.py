"""
    Problem: 70. Climbing Stairs
    Website: https://leetcode.com/problems/climbing-stairs/
    Difficulty: Easy
    Author: ZYZ
    Language: Python3
    Result: Accepted
    Runtime: 36 ms, faster than 66.40% of Python3 online submissions for Climbing Stairs.
    Memory Usage: 13.7 MB, less than 5.97% of Python3 online submissions for Climbing Stairs.
"""


class Solution:
    """
    You are climbing a stair case. It takes n steps to reach to the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

    Note: Given n will be a positive integer.
    """

    def climbStairs(self, n: int) -> int:
        # Fibonacci sequence
        r = [1, 1, 2]
        for i in range(n - 2):
            r[i % 3] = r[(i + 1) % 3] + r[(i + 2) % 3]

        return r[n % 3]


s = Solution()
a = 6
print(s.climbStairs(a))


"""
https://leetcode.com/problems/climbing-stairs/discuss/163347/Python-3000DP-or-tm

class Solution(object):
    def climbStairs(self, n):
        if n == 1: return 1
        a, b = 1, 2
        for _ in range(2, n):
            a, b = b, a + b
        return b


https://leetcode.com/problems/climbing-stairs/discuss/25296/3-4-short-lines-in-every-language
       
int climbStairs(int n) {
    int a = 1, b = 1;
    while (n--)
        a = (b += a) - a;
    return a;
}
"""

"""
https://leetcode.com/problems/climbing-stairs/discuss/25296/3-4-short-lines-in-every-language/188913
def climbStairs(self, n):
    return int((5**.5 / 5) * (((1 + 5**.5)/2)**(n + 1) - ((1 - 5**.5)/2)**(n + 1)))
"""

"""
快速幂算法
public class Solution {
   public int climbStairs(int n) {
       int[][] q = {{1, 1}, {1, 0}};
       int[][] res = pow(q, n);
       return res[0][0];
   }
   public int[][] pow(int[][] a, int n) {
       int[][] ret = {{1, 0}, {0, 1}};
       while (n > 0) {
           if ((n & 1) == 1) {
               ret = multiply(ret, a);
           }
           n >>= 1;
           a = multiply(a, a);
       }
       return ret;
   }
   public int[][] multiply(int[][] a, int[][] b) {
       int[][] c = new int[2][2];
       for (int i = 0; i < 2; i++) {
           for (int j = 0; j < 2; j++) {
               c[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j];
           }
       }
       return c;
   }
}

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/climbing-stairs/solution/pa-lou-ti-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""