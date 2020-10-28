# http://lx.lanqiao.cn/problem.page?gpid=T12


n = int(input())

if n <= 2:
    print(n)
elif n % 2 == 1:
    print(n * (n - 1) * (n - 2))
elif n % 3 == 0:
    print((n - 2) * (n - 1) * (n - 3))
else:
    print(n * (n - 1) * (n - 3))


# https://www.liuchuo.net/archives/1431
