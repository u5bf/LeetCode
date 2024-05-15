from itertools import accumulate

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        ans = -float('inf')
        for i in range(k):
            ans = max(ans, max(accumulate(reversed(energy[i::k]))))
        return ans
