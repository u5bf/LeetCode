#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#
# https://leetcode.cn/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (66.95%)
# Likes:    1930
# Dislikes: 0
# Total Accepted:    1M
# Total Submissions: 1.5M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
#
#
#
# 示例 1：
#
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[9,20],[15,7]]
#
#
# 示例 2：
#
#
# 输入：root = [1]
# 输出：[[1]]
#
#
# 示例 3：
#
#
# 输入：root = []
# 输出：[]
#
#
#
#
# 提示：
#
#
# 树中节点数目在范围 [0, 2000] 内
# -1000 <= Node.val <= 1000
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        deque = [root]
        ans = []
        last_node = root
        level = []
        cur_node = None
        while deque:
            node = deque.pop(0)
            if node.left:
                deque.append(node.left)
                cur_node = node.left
            if node.right:
                deque.append(node.right)
                cur_node = node.right
            level.append(node.val)
            if node == last_node:
                ans.append(level.copy())
                level = []
                last_node = cur_node
        return ans
# @lc code=end

