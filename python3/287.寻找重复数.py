#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#
# https://leetcode.cn/problems/find-the-duplicate-number/description/
#
# algorithms
# Medium (64.14%)
# Likes:    2376
# Dislikes: 0
# Total Accepted:    375.6K
# Total Submissions: 585.4K
# Testcase Example:  '[1,3,4,2,2]'
#
# 给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。
#
# 假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。
#
# 你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,3,4,2,2]
# 输出：2
#
#
# 示例 2：
#
#
# 输入：nums = [3,1,3,4,2]
# 输出：3
#
#
# 示例 3 :
#
#
# 输入：nums = [3,3,3,3,3]
# 输出：3
#
#
#
#
#
#
# 提示：
#
#
# 1 <= n <= 10^5
# nums.length == n + 1
# 1 <= nums[i] <= n
# nums 中 只有一个整数 出现 两次或多次 ，其余整数均只出现 一次
#
#
#
#
# 进阶：
#
#
# 如何证明 nums 中至少存在一个重复的数字?
# 你可以设计一个线性级时间复杂度 O(n) 的解决方案吗？
#
#
#


# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def next(i):
            return nums[i]
        slow = fast = 0
        # 第一次相遇
        while True:
            slow = next(slow)
            fast = next(next(fast))
            if slow == fast:
                break
        slow = 0
        # 第二次相遇
        while slow != fast:
            slow = next(slow)
            fast = next(fast)
        return slow
# @lc code=end
