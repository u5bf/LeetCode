#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#
# https://leetcode.cn/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (44.11%)
# Likes:    2305
# Dislikes: 0
# Total Accepted:    439.5K
# Total Submissions: 997K
# Testcase Example:  '[1,1,1]\n2'
#
# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。
#
# 子数组是数组中元素的连续非空序列。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,1,1], k = 2
# 输出：2
#
#
# 示例 2：
#
#
# 输入：nums = [1,2,3], k = 3
# 输出：2
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 2 * 10^4
# -1000 <= nums[i] <= 1000
# -10^7 <= k <= 10^7
#
#
#
# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        dic = {0:1}
        pre_sum = 0
        for num in nums:
            pre_sum += num
            if (diff_x := pre_sum - k) in dic:
                ans += dic[diff_x]
            dic[pre_sum] = dic.get(pre_sum, 0) + 1
        return ans
# @lc code=end

