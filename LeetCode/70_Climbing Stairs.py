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