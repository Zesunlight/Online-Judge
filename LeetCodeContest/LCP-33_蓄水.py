from math import ceil


class Solution:
    # https://leetcode-cn.com/problems/o8SXZn/

    def storeWater(self, bucket: List[int], vat: List[int]) -> int:
        change = 0
        n = len(bucket)
        full = [0 for _ in range(n)]

        for i in range(n):
            if bucket[i] == 0:
                if vat[i] != 0:
                    change += 1
                    bucket[i] += 1
                    full[i] = vat[i]
            else:
                full[i] = ceil(vat[i] / bucket[i])

        def arg_max(iter):
            if len(iter) == 0:
                return [-1]
            m = iter[0]
            p = [0]
            for i in range(1, len(iter)):
                if iter[i] > m:
                    p = [i]
                    m = iter[i]
                elif iter[i] == m:
                    p.append(i)
            return p

        which = arg_max(full)
        r = change + full[which[0]]
        while True:
            for w in which:
                bucket[w] += 1
                after = ceil(vat[w] / bucket[w])
                full[w] = after
            imagine = arg_max(full)

            temp = change + len(which) + full[imagine[0]]
            if temp <= r:
                change += len(which)
                r = temp
                which = imagine
            else:
                break
        return r

    def storeWater2(self, bucket: List[int], vat: List[int]) -> int:
        if sum(vat) == 0:
            return 0
        
        n = len(vat)
        ans = 10**4 + n

        for i in range(1, 10**4):
            res = i  # 倒 i 次水
            for j in range(n):
                res += max(0, ceil(vat[j] / i) - bucket[j])
            ans = min(ans, res)
        
        return ans
