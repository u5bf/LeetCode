# 当时没写出来
class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
    	nums.sort()
    	mid = len(nums) // 2
    	ans = 0
    	if nums[mid] < k:
    		for i in range(mid, len(nums)):
    			if nums[i] >= k:
    				break
    			ans += k - nums[i]
    	elif nums[mid] > k:
    		for i in range(mid, -1, -1):
    			if nums[i] <= k:
    				break
    			ans += nums[i] - k
    	return ans