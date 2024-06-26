#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#
# https://leetcode.cn/problems/subsets/description/
#
# algorithms
# Medium (81.26%)
# Likes:    2281
# Dislikes: 0
# Total Accepted:    778.1K
# Total Submissions: 957.5K
# Testcase Example:  '[1,2,3]'
#
# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
#
# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#
#
# 示例 2：
#
#
# 输入：nums = [0]
# 输出：[[],[0]]
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# nums 中的所有元素 互不相同
#
#
#
import copy
from typing import List
# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        n = len(nums)

        def dfs(level):
            ans.append(path.copy())
            for i in range(level, n):
                path.append(nums[i])
                dfs(i + 1)
                path.pop()

        dfs(0)
        return ans


# @lc code=end

Solution().subsets([1,2,3])
