"""
    Problem: 22. Generate Parentheses
    Website: https://leetcode.com/problems/generate-parentheses/
    Author: ZYZ
    Language: Python3
    Result: Accepted
    Runtime: 40 ms, faster than 77.89% of Python3 online submissions for Generate Parentheses.
    Memory Usage: 14 MB, less than 6.67% of Python3 online submissions for Generate Parentheses.
"""


class Solution:
    """
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

    For example, given n = 3, a solution set is:
    [
      "((()))",
      "(()())",
      "(())()",
      "()(())",
      "()()()"
    ]
    """

    def generateParenthesis(self, n: int):
        if n == 0:
            return []

        r = [['(', n-1, 1]]
        # result, how many '(' left, how many ')' need add

        for i in range(2, n+1):
            temp = []
            for j in r:
                if j[1] >= 1:
                    temp.append([j[0] + '(', j[1] - 1, j[2] + 1])

                    for k in range(1, j[2]+1):
                        temp.append([j[0] + ')' * k + '(', j[1] - 1, j[2] - k + 1])

            r = temp

        p = []
        for i in r:
            p.append(i[0] + ')' * i[2])

        return p


s = Solution()
a = 0
print(s.generateParenthesis(a))


"""
https://leetcode.com/problems/generate-parentheses/discuss/10105/Concise-recursive-C++-solution
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        addingpar(res, "", n, 0);
        return res;
    }
    void addingpar(vector<string> &v, string str, int n, int m){
        if(n==0 && m==0) {
            v.push_back(str);
            return;
        }
        if(m > 0){ addingpar(v, str+")", n, m-1); }
        if(n > 0){ addingpar(v, str+"(", n-1, m+1); }
    }
};
"""

"""
https://leetcode.com/problems/generate-parentheses/discuss/10127/An-iterative-method.

First consider how to get the result f(n) from previous result f(0)...f(n-1).
Actually, the result f(n) will be put an extra () pair to f(n-1). 
Let the "(" always at the first position, to produce a valid result, 
we can only put ")" in a way that there will be i pairs () inside the extra () and n - 1 - i pairs () outside the extra pair.
Let us consider an example to get clear view:
f(0): ""
f(1): "("f(0)")"
f(2): "("f(0)")"f(1), "("f(1)")"
f(3): "("f(0)")"f(2), "("f(1)")"f(1), "("f(2)")"
So f(n) = "("f(0)")"f(n-1) , "("f(1)")"f(n-2) "("f(2)")"f(n-3) ... "("f(i)")"f(n-1-i) ... "(f(n-1)")"

public class Solution
{
    public List<String> generateParenthesis(int n)
    {
        List<List<String>> lists = new ArrayList<>();
        lists.add(Collections.singletonList(""));
        
        for (int i = 1; i <= n; ++i)
        {
            final List<String> list = new ArrayList<>();
            
            for (int j = 0; j < i; ++j)
            {
                for (final String first : lists.get(j))
                {
                    for (final String second : lists.get(i - 1 - j))
                    {
                        list.add("(" + first + ")" + second);
                    }
                }
            }
            
            lists.add(list);
        }
        
        return lists.get(lists.size() - 1);
    }
}
"""

"""
https://leetcode.com/problems/generate-parentheses/discuss/10096/4-7-lines-Python
def generateParenthesis(self, n):
    def generate(p, left, right, parens=[]):
        if left:         generate(p + '(', left-1, right)
        if right > left: generate(p + ')', left, right-1)
        if not right:    parens += p,
        return parens
    return generate('', n, n)
"""