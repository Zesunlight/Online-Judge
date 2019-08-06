class Solution:
    def decodeString(self, s: str) -> str:
        left_bracket = s.find('[')
        if left_bracket == -1:
            return s

        right_bracket = len(s)
        bingo = 0
        for i in range(left_bracket+1, len(s)):
            if s[i] == '[':
                bingo += 1
            elif s[i] == ']':
                if bingo == 0:
                    right_bracket = i
                    break
                else:
                    bingo -= 1

        right_num = left_bracket
        left_num = left_bracket - 1
        while s[left_num].isdigit():
            left_num -= 1

        r = s[:left_num+1] + \
            eval(s[left_num+1:right_num]) * self.decodeString(s[left_bracket+1:right_bracket]) + \
            self.decodeString(s[right_bracket+1:])
        return r


s = Solution()
a = '30[u]'
print(s.decodeString(a))


'''
https://leetcode.com/problems/decode-string/discuss/87534/Simple-Java-Solution-using-Stack
public class Solution {
    public String decodeString(String s) {
        String res = "";
        Stack<Integer> countStack = new Stack<>();
        Stack<String> resStack = new Stack<>();
        int idx = 0;
        while (idx < s.length()) {
            if (Character.isDigit(s.charAt(idx))) {
                int count = 0;
                while (Character.isDigit(s.charAt(idx))) {
                    count = 10 * count + (s.charAt(idx) - '0');
                    idx++;
                }
                countStack.push(count);
            }
            else if (s.charAt(idx) == '[') {
                resStack.push(res);
                res = "";
                idx++;
            }
            else if (s.charAt(idx) == ']') {
                StringBuilder temp = new StringBuilder (resStack.pop());
                int repeatTimes = countStack.pop();
                for (int i = 0; i < repeatTimes; i++) {
                    temp.append(res);
                }
                res = temp.toString();
                idx++;
            }
            else {
                res += s.charAt(idx++);
            }
        }
        return res;
    }
}
'''

'''
https://leetcode.com/problems/decode-string/discuss/87662/Python-solution-using-stack
def decodeString(self, s):
    stack = []; curNum = 0; curString = ''
    for c in s:
        if c == '[':
            stack.append(curString)
            stack.append(curNum)
            curString = ''
            curNum = 0
        elif c == ']':
            num = stack.pop()
            prevString = stack.pop()
            curString = prevString + num*curString
        elif c.isdigit():
            curNum = curNum*10 + int(c)
        else:
            curString += c
    return curString
    
https://leetcode.com/problems/decode-string/discuss/87563/Share-my-Python-Stack-Simple-Solution-(Easy-to-understand)
def decodeString(self, s):
    stack = []
    stack.append(["", 1])
    num = ""
    for ch in s:
        if ch.isdigit():
          num += ch
        elif ch == '[':
            stack.append(["", int(num)])
            num = ""
        elif ch == ']':
            st, k = stack.pop()
            stack[-1][0] += st*k
        else:
            stack[-1][0] += ch
    return stack[0][0]
'''