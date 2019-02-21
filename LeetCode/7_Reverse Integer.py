"""
Author: ZYZ
Date: 2019.02.21
"""


class Solution:

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        r = ''
        f = 0
        if s[0] == '-':
            # negative
            f = -1
            for i in s[:0:-1]:
                r = r + i
        else:
            # positive
            for i in s[::-1]:
                r = r + i

        while r[0] == '0':
            if len(r) == 1:
                break
            r = r[1:]
        if f == -1:
            r = '-' + r

        n = int(r)
        if (n < -2147483648) or (n > 2147483647):
            n = 0

        return n

if __name__ == '__main__':
    c = Solution()
    print(c.reverse(-0))

"""
public int reverse(int x)
{
    int result = 0;

    while (x != 0)
    {
        int tail = x % 10;
        int newResult = result * 10 + tail;
        if ((newResult - tail) / 10 != result)
        { return 0; }
        result = newResult;
        x = x / 10;
    }

    return result;
}
"""

"""
def reverse(self, x):
    s = cmp(x, 0)
    r = int(str(s*x)[::-1])
    return s*r * (r < 2**31)
"""
