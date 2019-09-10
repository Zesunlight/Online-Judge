"""
    Problem: 76. Minimum Window Substring
    Website: https://leetcode.com/problems/minimum-window-substring/
    Difficulty: Hard
    Author: ZYZ
    Language: Python3
    Result: Accepted
    Runtime: 124 ms, faster than 73.33% of Python3 online submissions for Minimum Window Substring.
    Memory Usage: 14.5 MB, less than 5.55% of Python3 online submissions for Minimum Window Substring.
"""
import collections


class Solution:
    """
    Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
    """

    def minWindow(self, s: str, t: str) -> str:
        """
        If there is no such window in S that covers all characters in T, return the empty string "".
        If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
        """
        if not t:
            return ''

        calculate = collections.defaultdict(int)
        for i in t:
            calculate[i] += 1

        left, right = 0, 0
        required = len(t)
        res = s + '-'
        exist = False
        while right < len(s):
            if s[right] in t:
                if calculate[s[right]] > 0:
                    required -= 1
                calculate[s[right]] -= 1

            if required <= 0:
                exist = True
                temp = s[left:right+1]

                while (s[left] not in t) or (s[left] in t and calculate[s[left]] < 0):
                    temp = temp[1:]
                    if s[left] in t:
                        calculate[s[left]] += 1
                    left += 1
                else:
                    if len(temp) < len(res):
                        res = temp
                    required += 1
                    calculate[s[left]] += 1
                    left += 1
                    if left >= len(s):
                        return res

            right += 1

        return res if exist else ''


s = Solution()
S = "ADOBECODEBANC"
T = "ABC"
S = 'a'
T = ''
print(s.minWindow(S, T))


"""
https://www.youtube.com/watch?v=eS6PZLjoaq8&feature=youtu.be
"""

"""
https://leetcode.com/problems/minimum-window-substring/discuss/26808/Here-is-a-10-line-template-that-can-solve-most-'substring'-problems

string minWindow(string s, string t) {
        vector<int> map(128,0);
        for(auto c: t) map[c]++;
        int counter=t.size(), begin=0, end=0, d=INT_MAX, head=0;
        while(end<s.size()){
            if(map[s[end++]]-->0) counter--; //in t
            while(counter==0){ //valid
                if(end-begin<d)  d=end-(head=begin);
                if(map[s[begin++]]++==0) counter++;  //make it invalid
            }  
        }
        return d==INT_MAX? "":s.substr(head, d);
    }
    

template
int findSubstring(string s){
        vector<int> map(128,0);
        int counter; // check whether the substring is valid
        int begin=0, end=0; //two pointers, one point to tail and one  head
        int d; //the length of substring

        for() { /* initialize the hash map here */ }

        while(end<s.size()){

            if(map[s[end++]]-- ?){  /* modify counter here */ }

            while(/* counter condition */){ 
                 
                 /* update d here if finding minimum*/

                //increase begin to make it invalid/valid again
                
                if(map[s[begin++]]++ ?){ /*modify counter here*/ }
            }  

            /* update d here if finding maximum*/
        }
        return d;
  }
"""