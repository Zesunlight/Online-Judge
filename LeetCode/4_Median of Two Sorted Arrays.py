"""
Author: ZYZ
Date: 2019.02.21
"""


class Solution:
    '''leetcode'''

    def helper(self, num1, num2, a, b, c, d):
        r = 0

        if a > b:
            if ((d+c) / 2).is_integer():
                r = num2[int((d+c) / 2)]
            else:
                r = (num2[int((d+c+1) / 2)] + num2[int((d+c-1) / 2)]) / 2

        elif a == b:
            if ((d+c) / 2).is_integer():
                if num1[a] < num2[int((d+c) / 2) - 1]:
                    r = (num2[int((d+c) / 2)] + num2[int((d+c) / 2) - 1]) / 2
                elif num1[a] > num2[int((d+c) / 2) + 1]:
                    r = (num2[int((d+c) / 2)] + num2[int((d+c) / 2) + 1]) / 2
                else:
                    r = (num2[int((d+c) / 2)] + num1[a]) / 2
            else:
                # print((d+c-1)/2)
                if num1[a] < num2[int((d+c-1) / 2)]:
                    r = num2[int((d+c-1) / 2)]
                elif num1[a] > num2[int((d+c+1) / 2)]:
                    r = num2[int((d+c+1) / 2)]
                else:
                    r = num1[a]

        return r

    def findMedian(self, num1: 'List[int]', num2: 'List[int]') -> int:

        a, c = 0, 0
        b, d = len(num1) - 1, len(num2) - 1
        r = 0

        while (a < b) and (c < d):
            if num1[a] < num2[c]:
                a = a + 1
            else:
                c = c + 1

            if num1[b] < num2[d]:
                d = d - 1
            else:
                b = b - 1

        if (a == b) and (c == d):
            r = (num1[a] + num2[c]) / 2
        elif ((a == b) and (d == -1)):
            r = num1[a]
        elif ((c == d) and (b == -1)):
            r = num2[c]
        elif a >= b:
            r = self.helper(num1, num2, a, b, c, d)
        else:
            r = self.helper(num2, num1, c, d, a, b)

        if (r * 1.0).is_integer():
            r = int(r)

        return r


if __name__ == '__main__':
    c = Solution()
    a = [1, 2, 3]
    b = [1, 2, 2]
    print(c.findMedian(a, b))
