"""
    Problem: 32. Longest Valid Parentheses
    Website: https://leetcode.com/problems/longest-valid-parentheses/
    Author: ZYZ
    Language: Python3
    Result: Accepted
    Runtime: 56 ms, faster than 43.30% of Python3 online submissions for Longest Valid Parentheses.
    Memory Usage: 14.4 MB, less than 5.55% of Python3 online submissions for Longest Valid Parentheses.
"""


class Solution:
    """
    Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

    Example 1:

    Input: "(()"
    Output: 2
    Explanation: The longest valid parentheses substring is "()"

    Example 2:

    Input: ")()())"
    Output: 4
    Explanation: The longest valid parentheses substring is "()()"
    """

    def longestValidParentheses(self, s: str) -> int:
        stack = []
        longest = 0

        for index, i in enumerate(s):
            if i == '(':
                stack.append(index)
            elif i == ')':
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(index)

        print(stack)
        if stack:
            end = len(s)
            while stack:
                start = stack.pop()
                longest = max(longest, end - start - 1)
                end = start
            longest = max(longest, end)
        else:
            longest = len(s)

        return longest


s = Solution()
a = '())'
print(s.longestValidParentheses(a))


"""
https://leetcode.com/problems/longest-valid-parentheses/discuss/14126/My-O(n)-solution-using-a-stack

Scan the string from beginning to end.
If current character is '(', push its index to the stack. 
If current character is ')' and the character at the index of the top of stack is '(', we just find a matching pair so pop from the stack. 
Otherwise, we push the index of ')' to the stack.
After the scan is done, the stack will only contain the indices of characters which cannot be matched. 
Then let's use the opposite side - substring between adjacent indices should be valid parentheses.
If the stack is empty, the whole input string is valid. 
Otherwise, we can scan the stack to get longest valid substring as described in step 3.

class Solution {
public:
    int longestValidParentheses(string s) {
        int n = s.length(), longest = 0;
        stack<int> st;
        for (int i = 0; i < n; i++) {
            if (s[i] == '(') st.push(i);
            else {
                if (!st.empty()) {
                    if (s[st.top()] == '(') st.pop();
                    else st.push(i);
                }
                else st.push(i);
            }
        }
        if (st.empty()) longest = n;
        else {
            int a = n, b = 0;
            while (!st.empty()) {
                b = st.top(); st.pop();
                longest = max(longest, a-b-1);
                a = b;
            }
            longest = max(longest, a);
        }
        return longest;
    }
};
"""

"""
http://bangbingsyb.blogspot.com/2014/11/leetcode-longest-valid-parentheses.html

class Solution {
public:
    int longestValidParentheses(string s) {
        int n = s.size(), maxLen = 0;
        vector<int> dp(n+1,0);
        for(int i=1; i<=n; i++) {
            int j = i-2-dp[i-1];
            if(s[i-1]=='(' || j<0 || s[j]==')') 
                dp[i] = 0;
            else {
                dp[i] = dp[i-1]+2+dp[j];
                maxLen = max(maxLen, dp[i]);
            }
        }
        return maxLen;
    }
};


https://leetcode.com/problems/longest-valid-parentheses/discuss/14133/My-DP-O(n)-solution-without-using-stack

My solution uses DP. The main idea is as follows: I construct a array longest[], for any longest[i], it stores the longest length of valid parentheses which is end at i.
no need to consider the condition "s[i-1] == '('" since "s[i-longest[i-1]-1] == '('" actually concludes this case

int longestValidParentheses(string s) {
    if(s.length() <= 1) return 0;
    int curMax = 0;
    vector<int> longest(s.size(),0);
    for(int i=1; i < s.length(); i++){
        if(s[i] == ')' && i-longest[i-1]-1 >= 0 && s[i-longest[i-1]-1] == '('){
                longest[i] = longest[i-1] + 2 + ((i-longest[i-1]-2 >= 0)?longest[i-longest[i-1]-2]:0);
                curMax = max(longest[i],curMax);
        }
    }
    return curMax;
}
"""

"""
https://www.cnblogs.com/grandyang/p/4424731.html

class Solution {
public:
    int longestValidParentheses(string s) {
        int res = 0, start = 0;
        stack<int> m;
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == '(') m.push(i);
            else if (s[i] == ')') {
                if (m.empty()) start = i + 1;
                else {
                    m.pop();
                    res = m.empty() ? max(res, i - start + 1) : max(res, i - m.top());
                }
            }
        }
        return res;
    }
};
"""