# http://lx.lanqiao.cn/problem.page?gpid=T445


n = int(input())
res = ''
while n > 0:
    n, r = divmod(n, 26)
    if r == 0:
        res += 'Z'
        n -= 1
    else:
        res += chr(ord('A') - 1 + r)
print(res[::-1])
