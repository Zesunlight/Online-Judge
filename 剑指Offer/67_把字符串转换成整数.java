/*
=================================================
Problem: 面试题 67. 把字符串转换成整数
Website: https://leetcode-cn.com/problems/ba-zi-fu-chuan-zhuan-huan-cheng-zheng-shu-lcof/
Difficulty: 简单
Author: ZYZ
Language: Java
Result: Accepted
Runtime: 4 ms, 在所有 Python3 提交中击败了9.69%的用户
Memory Usage: 40 MB, 在所有 Python3 提交中击败了5.02%的用户
==================================================*/


class Solution {
    public int strToInt(String str) {
        StringBuilder r = new StringBuilder();
        boolean nextInt = false;
        for (int i = 0; i < str.length(); i++) {
            if (nextInt) {
                if (str.charAt(i) >= '0' && str.charAt(i) <= '9') {
                    r.append(str.charAt(i));

                    long res = Long.parseLong(r.toString());
                    if (res > Integer.MAX_VALUE) return Integer.MAX_VALUE;
                    else if (res < Integer.MIN_VALUE) return Integer.MIN_VALUE;

                    continue;
                }
                else break;
            }
            if (str.charAt(i) == ' ') continue;
            else if (str.charAt(i) == '-' || str.charAt(i) == '+') {
                r.append(str.charAt(i));
                nextInt = true;
            } else if (str.charAt(i) >= '0' && str.charAt(i) <= '9') {
                r.append(str.charAt(i));
                nextInt = true;
            } else return 0;
        }

        try {
            long res = Long.parseLong(r.toString());
            if (res <= Integer.MAX_VALUE && res >= Integer.MIN_VALUE)
                return Integer.parseInt(r.toString());
            else if (res > Integer.MAX_VALUE) return Integer.MAX_VALUE;
            else return Integer.MIN_VALUE;
        } catch (Exception e) {
            return 0;
        }
    }
}


class Solution2 {
    public int strToInt(String str) {
        char[] c = str.trim().toCharArray();
        if(c.length == 0) return 0;
        int res = 0, bndry = Integer.MAX_VALUE / 10;
        int i = 1, sign = 1;
        if(c[0] == '-') sign = -1;
        else if(c[0] != '+') i = 0;
        for(int j = i; j < c.length; j++) {
            if(c[j] < '0' || c[j] > '9') break;
            if(res > bndry || res == bndry && c[j] > '7') return sign == 1 ? Integer.MAX_VALUE : Integer.MIN_VALUE;
            res = res * 10 + (c[j] - '0');
        }
        return sign * res;
    }
}


class Solution3 {
    public int strToInt(String str) {
        int res = 0, bndry = Integer.MAX_VALUE / 10;
        int i = 0, sign = 1, length = str.length();
        if(length == 0) return 0;
        while(str.charAt(i) == ' ')
            if(++i == length) return 0;
        if(str.charAt(i) == '-') sign = -1;
        if(str.charAt(i) == '-' || str.charAt(i) == '+') i++;
        for(int j = i; j < length; j++) {
            if(str.charAt(j) < '0' || str.charAt(j) > '9') break;
            if(res > bndry || res == bndry && str.charAt(j) > '7')
                return sign == 1 ? Integer.MAX_VALUE : Integer.MIN_VALUE;
            res = res * 10 + (str.charAt(j) - '0');
        }
        return sign * res;
    }
}

// 作者：jyd
// 链接：https://leetcode-cn.com/problems/ba-zi-fu-chuan-zhuan-huan-cheng-zheng-shu-lcof/solution/mian-shi-ti-67-ba-zi-fu-chuan-zhuan-huan-cheng-z-4/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。