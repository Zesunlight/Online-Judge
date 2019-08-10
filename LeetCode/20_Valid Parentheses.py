class Solution:
    """
    20. Valid Parentheses
    Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Note that an empty string is also considered valid.
    """

    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True

        stack = []
        left = ['(', '{', '[']
        right = [')', '}', ']']

        for bracket in s:
            if bracket in left:
                stack.append(left.index(bracket))
            elif bracket in right:
                if stack and right.index(bracket) == stack[-1]:
                    stack.pop()
                else:
                    return False

        return stack == []


s = Solution()
example = '{(}'
print(s.isValid(example))


"""
https://leetcode.com/problems/valid-parentheses/discuss/9203/Simple-Python-solution-with-stack
def isValid(self, s):
    stack = []
    dict = {"]":"[", "}":"{", ")":"("}
    for char in s:
        if char in dict.values():
            stack.append(char)
        elif char in dict.keys():
            if stack == [] or dict[char] != stack.pop():
                return False
        else:
            return False
    return stack == []
"""

"""
https://leetcode.com/problems/valid-parentheses/discuss/9225/Python-is-this-a-cheating-method-accepted-with-40ms-easy-to-understand-but
def isValid(self, s):
    n = len(s)
    if n == 0:
        return True
    
    if n % 2 != 0:
        return False
        
    while '()' in s or '{}' in s or '[]' in s:
        s = s.replace('{}','').replace('()','').replace('[]','')
    
    if s == '':
        return True
    else:
        return False
"""

"""
https://leetcode.com/problems/valid-parentheses/discuss/9252/2ms-C++-sloution
#include <stack>

class Solution {
public:
    bool isValid(string s) {
        stack<char> paren;
        for (char& c : s) {
            switch (c) {
                case '(': 
                case '{': 
                case '[': paren.push(c); break;
                case ')': if (paren.empty() || paren.top()!='(') return false; else paren.pop(); break;
                case '}': if (paren.empty() || paren.top()!='{') return false; else paren.pop(); break;
                case ']': if (paren.empty() || paren.top()!='[') return false; else paren.pop(); break;
                default: ; // pass
            }
        }
        return paren.empty() ;
    }
};


https://leetcode.com/problems/valid-parentheses/discuss/9222/My-0ms-c++-solution-using-stack
bool isValid(string s) {
    stack<char> st;
    for(char c : s){
        if(c == '('|| c == '{' || c == '['){
            st.push(c);
        }else{
            if(st.empty()) return false;
            if(c == ')' && st.top() != '(') return false;
            if(c == '}' && st.top() != '{') return false;
            if(c == ']' && st.top() != '[') return false;
            st.pop();
        }
    }
    return st.empty();
"""