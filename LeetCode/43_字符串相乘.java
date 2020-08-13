import java.util.*;

/*
    43. 字符串相乘
    https://leetcode-cn.com/problems/multiply-strings/

    给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

    执行用时：27 ms, 在所有 Java 提交中击败了16.92%的用户
    内存消耗：40.4 MB, 在所有 Java 提交中击败了10.81%的用户
 */


class Solution {
    public String multiply(String num1, String num2) {
        if (num1.equals("0") || num2.equals("0")) return "0";
        if (num1.length() < num2.length()) return multiply(num2, num1);
        String result = "";
        StringBuilder zero = new StringBuilder();
        for (int i = num2.length() - 1; i >= 0; i--) {
            result = add(result, multiply(num1, num2.charAt(i)) + zero);
            zero.append('0');
        }
        return result;
    }

    public String multiply(String num, char c) {
        StringBuilder res = new StringBuilder();
        int carry = 0;
        for (int i = num.length() - 1; i >= 0; i--) {
            int temp = (num.charAt(i) - '0') * (c - '0') + carry;
            carry = temp / 10;
            res.append(temp % 10);
        }
        if (carry > 0) res.append(carry);
        return res.reverse().toString();
    }

    public String add(String a, String b) {
        if (a.length() < b.length()) return add(b, a);

        StringBuilder res = new StringBuilder();
        int carry = 0;
        for (int i = 1; i <= b.length(); i++) {
            int temp = b.charAt(b.length() - i) - '0' + a.charAt(a.length() - i) - '0' + carry;
            carry = temp / 10;
            res.append(temp % 10);
        }

        for (int i = a.length() - b.length() - 1; i >= 0; i--) {
            int temp = a.charAt(i) - '0' + carry;
            carry = temp / 10;
            res.append(temp % 10);
        }

        if (carry > 0) res.append(carry);
        return res.reverse().toString();
    }
}


class Solution {
    public String multiply(String num1, String num2) {
        if (num1.equals("0") || num2.equals("0")) {
            return "0";
        }
        String ans = "0";
        int m = num1.length(), n = num2.length();
        for (int i = n - 1; i >= 0; i--) {
            StringBuffer curr = new StringBuffer();
            int add = 0;
            for (int j = n - 1; j > i; j--) {
                curr.append(0);
            }
            int y = num2.charAt(i) - '0';
            for (int j = m - 1; j >= 0; j--) {
                int x = num1.charAt(j) - '0';
                int product = x * y + add;
                curr.append(product % 10);
                add = product / 10;
            }
            if (add != 0) {
                curr.append(add % 10);
            }
            ans = addStrings(ans, curr.reverse().toString());
        }
        return ans;
    }

    public String addStrings(String num1, String num2) {
        int i = num1.length() - 1, j = num2.length() - 1, add = 0;
        StringBuffer ans = new StringBuffer();
        while (i >= 0 || j >= 0 || add != 0) {
            int x = i >= 0 ? num1.charAt(i) - '0' : 0;
            int y = j >= 0 ? num2.charAt(j) - '0' : 0;
            int result = x + y + add;
            ans.append(result % 10);
            add = result / 10;
            i--;
            j--;
        }
        ans.reverse();
        return ans.toString();
    }
}

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/multiply-strings/solution/zi-fu-chuan-xiang-cheng-by-leetcode-solution/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution {
    public String multiply(String num1, String num2) {
        if (num1.equals("0") || num2.equals("0")) {
            return "0";
        }
        int m = num1.length(), n = num2.length();
        int[] ansArr = new int[m + n];
        for (int i = m - 1; i >= 0; i--) {
            int x = num1.charAt(i) - '0';
            for (int j = n - 1; j >= 0; j--) {
                int y = num2.charAt(j) - '0';
                ansArr[i + j + 1] += x * y;
            }
        }
        for (int i = m + n - 1; i > 0; i--) {
            ansArr[i - 1] += ansArr[i] / 10;
            ansArr[i] %= 10;
        }
        int index = ansArr[0] == 0 ? 1 : 0;
        StringBuffer ans = new StringBuffer();
        while (index < m + n) {
            ans.append(ansArr[index]);
            index++;
        }
        return ans.toString();
    }
}

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/multiply-strings/solution/zi-fu-chuan-xiang-cheng-by-leetcode-solution/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。