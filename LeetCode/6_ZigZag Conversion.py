class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows >= len(s) or numRows == 1:
            return s

        sz = s[::2*numRows-2]
        for i in range(1, numRows - 1):
            sz += s[i]
            for j in range(2*numRows-i-2, len(s), 2*numRows-2):
                sz += s[j]
                if j+2*i < len(s):
                    sz += s[j+2*i]
        sz += s[numRows-1::2*numRows-2]

        return sz

a = Solution()
print(a.convert("PAYPALISHIRING", 3))

'''
https://leetcode.com/problems/zigzag-conversion/discuss/3435/If-you-are-confused-with-zigzag-patterncome-and-see!
n=numRows
Δ=2n-2    1                           2n-1                         4n-3
Δ=        2                     2n-2  2n                    4n-4   4n-2
Δ=        3               2n-3        2n+1              4n-5       .
Δ=        .           .               .               .            .
Δ=        .       n+2                 .           3n               .
Δ=        n-1 n+1                     3n-3    3n-1                 5n-5
Δ=2n-2    n                           3n-2                         5n-4


Easy to understand Java solution
https://leetcode.com/problems/zigzag-conversion/discuss/3403/Easy-to-understand-Java-solution

public String convert(String s, int nRows) {
    char[] c = s.toCharArray();
    int len = c.length;
    StringBuffer[] sb = new StringBuffer[nRows];
    for (int i = 0; i < sb.length; i++) sb[i] = new StringBuffer();

    int i = 0;
    while (i < len) {
        for (int idx = 0; idx < nRows && i < len; idx++) // vertically down
            sb[idx].append(c[i++]);
        for (int idx = nRows-2; idx >= 1 && i < len; idx--) // obliquely up
            sb[idx].append(c[i++]);
    }
    for (int idx = 1; idx < sb.length; idx++)
        sb[0].append(sb[idx]);
    return sb[0].toString();
}
'''