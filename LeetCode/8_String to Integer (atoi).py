class Solution:
    def my_atoi(self, str: str) -> int:
        num = '0'
        s = str.lstrip()

        if not s:
            return 0

        if s[0] == '-' or s[0] == '+':
            num = s[0]
            s = s[1:]

        for i in s:
            if i.isdigit():
                num += i
            else:
                break

        if not num[0].isdigit() and len(num) == 1:
            num = '0'

        n = int(num)
        n = min(n, 2 ** 31 -1)
        n = max(n, - 2 ** 31)

        return n


s = Solution()
example = '0+1'

print(s.my_atoi(example))


'''
https://leetcode.com/problems/string-to-integer-atoi/discuss/4642/8ms-C++-solution-easy-to-understand
int myAtoi(string str) {
    long result = 0;
    int indicator = 1;
    for(int i = 0; i<str.size();)
    {
        i = str.find_first_not_of(' ');
        if(str[i] == '-' || str[i] == '+')
            indicator = (str[i++] == '-')? -1 : 1;
        while('0'<= str[i] && str[i] <= '9') 
        {
            result = result*10 + (str[i++]-'0');
            if(result*indicator >= INT_MAX) return INT_MAX;
            if(result*indicator <= INT_MIN) return INT_MIN;                
        }
        return result*indicator;
    }
}
'''