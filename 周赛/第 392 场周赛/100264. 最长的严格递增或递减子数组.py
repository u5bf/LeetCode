class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        def check(nums):
            n = len(nums)
            dp = [1] * n
            for i in range(1, n):
                if nums[i] > nums[i - 1]:
                    dp[i] = dp[i - 1] + 1
            return max(dp)
        return max(check(nums),check(nums[::-1]))