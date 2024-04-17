#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#
# https://leetcode.cn/problems/permutations-ii/description/
#
# algorithms
# Medium (65.69%)
# Likes:    1555
# Dislikes: 0
# Total Accepted:    536.4K
# Total Submissions: 816.6K
# Testcase Example:  '[1,1,2]'
#
# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,1,2]
# 输出：
# [[1,1,2],
# ⁠[1,2,1],
# ⁠[2,1,1]]
#
#
# 示例 2：
#
#
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10
#
#
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        state = []
        n = len(nums)
        seen = [False] * n
        def dfs():
            if len(state) == n:
                res.append(list(state))
                return

            visited = set()
            for i in range(n):
                if seen[i] == False and nums[i] not in visited:
                    seen[i] = True
                    state.append(nums[i])
                    visited.add(nums[i])
                    dfs()
                    seen[i] = False
                    state.pop()

        dfs()
        return res
# @lc code=end

