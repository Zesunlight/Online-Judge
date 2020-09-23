# https://leetcode-cn.com/problems/er94lq/

class Solution:
    def isMagic(self, target: List[int]) -> bool:
        n = len(target)
        for i in range(1, n + 1):
            if self.from_to(list(range(1, n + 1)), target, i):
                return True
        return False

    def from_to(self, src, dst, k):
        new_src = self.change(src)
        if self.same(new_src, dst, k):
            if k >= len(dst):
                return True
            return self.from_to(new_src[k:], dst[k:], k)
        else:
            return False

    def change(self, cards):
        odd = cards[::2]
        even = cards[1::2]
        return even + odd

    def same(self, src, dst, k):
        for i in range(min(k, len(src))):
            if src[i] != dst[i]:
                return False
        return True