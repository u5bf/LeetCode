#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#
# https://leetcode.cn/problems/first-missing-positive/description/
#
# algorithms
# Hard (44.26%)
# Likes:    2087
# Dislikes: 0
# Total Accepted:    376.3K
# Total Submissions: 848.3K
# Testcase Example:  '[1,2,0]'
#
# 给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
# 请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,2,0]
# 输出：3
# 解释：范围 [1,2] 中的数字都在数组中。
#
# 示例 2：
#
#
# 输入：nums = [3,4,-1,1]
# 输出：2
# 解释：1 在数组中，但 2 没有。
#
# 示例 3：
#
#
# 输入：nums = [7,8,9,11,12]
# 输出：1
# 解释：最小的正数 1 没有出现。
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10^5
# -2^31 <= nums[i] <= 2^31 - 1
#
#
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
# @lc code=end

