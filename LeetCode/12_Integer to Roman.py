"""
    Problem: 12. Integer to Roman
    Website: https://leetcode.com/problems/integer-to-roman/
    Difficulty: Medium
    Author: ZYZ
    Language: Python3
    Result: Accepted
    Runtime: 48 ms, faster than 67.34% of Python3 online submissions for Integer to Roman.
    Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Integer to Roman.
"""


class Solution:
    """
    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
    """
    def intToRoman(self, num: int) -> str:
        res = ""
        Roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        digit = 1
        while num:
            a = num % 10
            num = num // 10

            if a == 4:
                res = Roman[digit - 1] + Roman[digit] + res
            elif a == 9:
                res = Roman[digit - 1] + Roman[digit + 1] + res
            elif 0 <= a <= 3:
                res = Roman[digit - 1] * a + res
            else:
                res = Roman[digit] + Roman[digit - 1] * (a - 5) + res
            digit += 2

        return res


"""
https://leetcode.com/problems/integer-to-roman/discuss/6274/Simple-Solution

public static String intToRoman(int num) {
    String M[] = {"", "M", "MM", "MMM"};
    String C[] = {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
    String X[] = {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
    String I[] = {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};
    return M[num/1000] + C[(num%1000)/100] + X[(num%100)/10] + I[num%10];
}
"""
