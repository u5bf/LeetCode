#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#
# https://leetcode.cn/problems/majority-element/description/
#
# algorithms
# Easy (66.32%)
# Likes:    2181
# Dislikes: 0
# Total Accepted:    916.9K
# Total Submissions: 1.4M
# Testcase Example:  '[3,2,3]'
#
# 给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
#
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
#
#
#
# 示例 1：
#
#
# 输入：nums = [3,2,3]
# 输出：3
#
# 示例 2：
#
#
# 输入：nums = [2,2,1,1,1,2,2]
# 输出：2
#
#
#
# 提示：
#
#
# n == nums.length
# 1 <= n <= 5 * 10^4
# -10^9 <= nums[i] <= 10^9
#
#
#
#
# 进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。
#
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
# @lc code=end

