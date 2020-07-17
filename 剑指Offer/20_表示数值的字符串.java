import java.util.*;

/*
    20. 表示数值的字符串
    https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/

    请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
    例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"0123"都表示数值，但"12e"、"1a3.14"、"1.2.3"、"+-5"、"-1E-16"及"12e+5.4"都不是。

    执行用时：3 ms, 在所有 Java 提交中击败了55.32%的用户
    内存消耗：40.3 MB, 在所有 Java 提交中击败了100.00%的用户
 */


class Solution {

    public boolean isNumber(String s) {
        boolean canPoint = true, canSign = true, canE = true;
        s = s.strip();
        if (s.equals("") || s.equals(".")) return false;

        for (int i = 0; i < s.length(); ++i) {
            if (isSign(s.charAt(i))) {
                if (!canSign) return false;
                if (i < s.length() - 1 && (isNumberCharacter(s.charAt(i + 1)) || s.charAt(i + 1) == '.')) {
                    canSign = false;
                } else return false;
            } else if (s.charAt(i)== '.') {
                if (!canPoint) return false;
                if ((i == s.length() - 1 && isNumberCharacter(s.charAt(i - 1))) ||
                        (i < s.length() - 1 && (isNumberCharacter(s.charAt(i + 1)) || s.charAt(i + 1) == 'e'))) {
                    canPoint = false;
                } else return false;
            } else if (s.charAt(i)== 'e') {
                if (!canE) return false;
                if (i > 0 && (s.charAt(i - 1) == '.')) {
                    if (!(i > 1 && isNumberCharacter(s.charAt(i - 2)))) return false;
                } else if (!(i > 0 && isNumberCharacter(s.charAt(i - 1)))) return false;

                if (i < s.length() - 1 && (isNumberCharacter(s.charAt(i + 1)) || isSign(s.charAt(i + 1)))) {
                    canE = false;
                    canSign = true;
                    canPoint = false;
                } else return false;
            } else if (s.charAt(i)>= '0' && s.charAt(i)<= '9') {
                canSign = false;
            } else {
                return false;
            }
        }

        return true;
    }

    public boolean isNumberCharacter(char a) {
        return a >= '0' && a <= '9';
    }

    public boolean isSign(char a) {
        return a == '-' || a == '+';
    }

}


/*
class Solution:
    def isNumber(self, s: str) -> bool:
        states = [
            { ' ': 0, 's': 1, 'd': 2, '.': 4 }, # 0. start with 'blank'
            { 'd': 2, '.': 4 } ,                # 1. 'sign' before 'e'
            { 'd': 2, '.': 3, 'e': 5, ' ': 8 }, # 2. 'digit' before 'dot'
            { 'd': 3, 'e': 5, ' ': 8 },         # 3. 'digit' after 'dot'
            { 'd': 3 },                         # 4. 'digit' after 'dot' (‘blank’ before 'dot')
            { 's': 6, 'd': 7 },                 # 5. 'e'
            { 'd': 7 },                         # 6. 'sign' after 'e'
            { 'd': 7, ' ': 8 },                 # 7. 'digit' after 'e'
            { ' ': 8 }                          # 8. end with 'blank'
        ]
        p = 0                           # start with state 0
        for c in s:
            if '0' <= c <= '9': t = 'd' # digit
            elif c in "+-": t = 's'     # sign
            elif c in ".eE ": t = c     # dot, e, blank
            else: t = '?'               # unknown
            if t not in states[p]: return False
            p = states[p][t]
        return p in (2, 3, 7, 8)
*/


class Solution2 {
    public boolean isNumber(String s) {
        Map[] states = {
            new HashMap<>() {{ put(' ', 0); put('s', 1); put('d', 2); put('.', 4); }}, // 0.
            new HashMap<>() {{ put('d', 2); put('.', 4); }},                           // 1.
            new HashMap<>() {{ put('d', 2); put('.', 3); put('e', 5); put(' ', 8); }}, // 2.
            new HashMap<>() {{ put('d', 3); put('e', 5); put(' ', 8); }},              // 3.
            new HashMap<>() {{ put('d', 3); }},                                        // 4.
            new HashMap<>() {{ put('s', 6); put('d', 7); }},                           // 5.
            new HashMap<>() {{ put('d', 7); }},                                        // 6.
            new HashMap<>() {{ put('d', 7); put(' ', 8); }},                           // 7.
            new HashMap<>() {{ put(' ', 8); }}                                         // 8.
        };
        int p = 0;
        char t;
        for(char c : s.toCharArray()) {
            if(c >= '0' && c <= '9') t = 'd';
            else if(c == '+' || c == '-') t = 's';
            else if(c == '.' || c == 'e' || c == 'E' || c == ' ') t = c;
            else t = '?';
            if(!states[p].containsKey(t)) return false;
            p = (int)states[p].get(t);
        }
        return p == 2 || p == 3 || p == 7 || p == 8;
    }
}

// 作者：jyd
// 链接：https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/solution/mian-shi-ti-20-biao-shi-shu-zhi-de-zi-fu-chuan-y-2/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution3 {
    public boolean isNumber(String s) {
        if(s == null || s.length() == 0){
            return false;
        }
        //标记是否遇到相应情况
        boolean numSeen = false;
        boolean dotSeen = false;
        boolean eSeen = false;
        char[] str = s.trim().toCharArray();
        for(int i = 0;i < str.length; i++){
            if(str[i] >= '0' && str[i] <= '9'){
                numSeen = true;
            }else if(str[i] == '.'){
                //.之前不能出现.或者e
                if(dotSeen || eSeen){
                    return false;
                }
                dotSeen = true;
            }else if(str[i] == 'e' || str[i] == 'E'){
                //e之前不能出现e，必须出现数
                if(eSeen || !numSeen){
                    return false;
                }
                eSeen = true;
                numSeen = false;//重置numSeen，排除123e或者123e+的情况,确保e之后也出现数
            }else if(str[i] == '-' || str[i] == '+'){
                //+-出现在0位置或者e/E的后面第一个位置才是合法的
                if(i != 0 && str[i-1] != 'e' && str[i-1] != 'E'){
                    return false;
                }
            }else{//其他不合法字符
                return false;
            }
        }
        return numSeen;
    }
}

// 作者：yangshyu6
// 链接：https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/solution/javaban-ben-ti-jie-luo-ji-qing-xi-by-yangshyu6/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


/*
class Solution:
    def isNumber(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False
*/
// https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/comments/255613