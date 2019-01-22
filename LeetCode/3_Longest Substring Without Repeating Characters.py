"""
Author: ZYZ
Date: 2019.01.22
"""


class Solution:
    """
    https://leetcode.com/problems/
            longest-substring-without-repeating-characters/
    """

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sup = len(set(s))
        if sup == 1:
            return 1
        elif sup == len(s):
            return sup

        r = 0

        for i in range(len(s) - 1):
            sup_j = min(i + sup, len(s))
            for j in range(i + 1, sup_j):
                if s[j] in s[i:j]:
                    break
                else:
                    if r < j - i + 1:
                        r = j - i + 1
        return r

c = Solution()
print(c.lengthOfLongestSubstring('abcdefc'))

"""
public int lengthOfLongestSubstring(String s) {
        if (s.length()==0) return 0;
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        int max=0;
        for (int i=0, j=0; i<s.length(); ++i){
            if (map.containsKey(s.charAt(i))){
                j = Math.max(j,map.get(s.charAt(i))+1);
            }
            map.put(s.charAt(i),i);
            max = Math.max(max,i-j+1);
        }
        return max;
    }
"""

"""
    def lengthOfLongest(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        longest = 0
        i = j = 0
        while i < len(s):
            if s[i] in d:
                j = max(j, d[s[i]] + 1)
            d[s[i]] = i
            longest = max(longest, i-j+1)
            i += 1

        return longest
"""