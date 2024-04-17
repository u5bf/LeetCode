#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#
# https://leetcode.cn/problems/diameter-of-binary-tree/description/
#
# algorithms
# Easy (59.95%)
# Likes:    1518
# Dislikes: 0
# Total Accepted:    411.5K
# Total Submissions: 684.9K
# Testcase Example:  '[1,2,3,4,5]'
#
# 给你一棵二叉树的根节点，返回该树的 直径 。
#
# 二叉树的 直径 是指树中任意两个节点之间最长路径的 长度 。这条路径可能经过也可能不经过根节点 root 。
#
# 两节点之间路径的 长度 由它们之间边数表示。
#
#
#
# 示例 1：
#
#
# 输入：root = [1,2,3,4,5]
# 输出：3
# 解释：3 ，取路径 [4,2,1,3] 或 [5,2,1,3] 的长度。
#
#
# 示例 2：
#
#
# 输入：root = [1,2]
# 输出：1
#
#
#
#
# 提示：
#
#
# 树中节点数目在范围 [1, 10^4] 内
# -100 <= Node.val <= 100
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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = -1

        def height(node):
            if not node:
                return 0
            lh = height(node.left)
            rh = height(node.right)
            self.ans = max(self.ans, lh + rh)
            return max(lh, rh) + 1

        height(root)
        return self.ans


# @lc code=end
