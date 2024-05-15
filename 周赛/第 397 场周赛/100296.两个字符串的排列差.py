class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        ans = 0
        temp = list(t)
        for i, v in enumerate(s):
            ans += abs(i - temp.index(v))
        return ans
