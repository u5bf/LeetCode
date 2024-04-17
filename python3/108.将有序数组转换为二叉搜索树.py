#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#
# https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/description/
#
# algorithms
# Easy (78.26%)
# Likes:    1498
# Dislikes: 0
# Total Accepted:    463.3K
# Total Submissions: 591.5K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# 给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 平衡 二叉搜索树。
#
#
#
# 示例 1：
#
#
# 输入：nums = [-10,-3,0,5,9]
# 输出：[0,-3,9,-10,null,5]
# 解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：
#
#
#
# 示例 2：
#
#
# 输入：nums = [1,3]
# 输出：[3,1]
# 解释：[1,null,3] 和 [3,1] 都是高度平衡二叉搜索树。
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums 按 严格递增 顺序排列
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(l, r):
            if l >= r: return None
            mid = (l + r) // 2
            # 总是选择中间位置左边的数字作为根节点
            node = TreeNode(nums[mid])
            node.left = dfs(l, mid)
            node.right = dfs(mid+1, r)
            return node

        return dfs(0, len(nums))

# @lc code=end

