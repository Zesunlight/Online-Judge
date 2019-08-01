class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s is None:
            return ''

        length = 0
        left, right = 0, len(s)

        for end in range(len(s) - 1, -1, -1):
            if end + 1 <= length:
                break
            start = s.find(s[end])
            while start != -1:
                if self.palindrome(s[start:end+1]):
                    if end + 1 - start > length:
                        left = start
                        right = end + 1
                        length = end + 1 - start
                    break
                else:
                    # print(s[start + 1:])
                    start = s.find(s[end], start+1)

        return s[left:right]

    def palindrome(self, s):
        if s == s[::-1]:
            return True
        else:
            return False


s = Solution()
example = 'cadfghj'

print(s.longestPalindrome(example))


'''
https://leetcode.com/problems/longest-palindromic-substring/discuss/2954/Python-easy-to-understand-solution-with-comments-(from-middle-to-two-ends).
def longestPalindrome(self, s):
    res = ""
    for i in xrange(len(s)):
        # odd case, like "aba"
        tmp = self.helper(s, i, i)
        if len(tmp) > len(res):
            res = tmp
        # even case, like "abba"
        tmp = self.helper(s, i, i+1)
        if len(tmp) > len(res):
            res = tmp
    return res
 
# get the longest palindrome, l, r are the middle indexes   
# from inner to outer
def helper(self, s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1; r += 1
    return s[l+1:r]

'''