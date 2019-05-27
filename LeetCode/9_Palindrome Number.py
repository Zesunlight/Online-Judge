class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        for i in range(len(s) // 2):
            if s[i] == s[len(s) - i - 1]:
                continue
            else:
                return False
        return True

    # return False if x < 0 else x == int(str(x)[::-1])

a = Solution()
print(a.isPalindrome(1))