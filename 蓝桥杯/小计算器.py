# http://lx.lanqiao.cn/problem.page?gpid=T459


def base(n, b):
    # 十进制转b进制

    # ************************ 坑点所在
    if n == 0:
        return '0'
    # ************************

    trans = [str(i) for i in range(10)]
    trans.extend([chr(i) for i in range(ord('A'), ord('Z') + 1)])
    res = ''
    while n:
        n, r = divmod(n, b)
        res += trans[r]
    return res[::-1]

n = int(input())
cur_base, result = 10, 0
caculate = ''
for _ in range(n):
    order = input()
    if order.startswith('N'):
        _, a = order.split()
        a = int(a, cur_base)

        if caculate != '':
            if caculate.startswith('A'):
                result += a
            elif caculate.startswith('S'):
                result -= a
            elif caculate.startswith('MU'):
                result *= a
            elif caculate.startswith('D'):
                result //= a
            elif caculate.startswith('MO'):
                result %= a
        else:
            result = a
    elif order.startswith('CH'):
        _, b = order.split()
        cur_base = int(b)
    elif order.startswith('CL'):
        result = 0
        caculate = ''
    elif order.startswith('E'):
        if cur_base == 10:
            print(result)
        else:
            print(base(result, cur_base))
    else:
        caculate = order
