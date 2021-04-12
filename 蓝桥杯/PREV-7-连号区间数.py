# http://lx.lanqiao.cn/problem.page?gpid=T30


n = int(input())
nums = list(map(int, input().split()))

ans = 0
for i in range(n):
    small, large = nums[i], nums[i]
    for j in range(i+1, n):
        small = min(small, nums[j])
        large = max(large, nums[j])
        if (large - small) == (j - i):
            ans += 1
print(ans + n)  # 过80%，最后一个超时，貌似C++可以全过
