# 当时没写出来
class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        t = list(s)
        for i, c in enumerate(map(ord, s)):
            dis = min(c - ord("a"), ord("z") - c + 1)
            if dis > k:
                t[i] = chr(c - k)
                break
            t[i] = "a"
            k -= dis
        return "".join(t)
