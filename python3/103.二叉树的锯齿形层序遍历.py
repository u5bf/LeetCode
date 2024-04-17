#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
#
# https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (58.76%)
# Likes:    870
# Dislikes: 0
# Total Accepted:    366.7K
# Total Submissions: 624K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
#
#
#
# 示例 1：
#
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[20,9],[15,7]]
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
# -100 <= Node.val <= 100
#
#
#
import collections
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        deque = collections.deque()
        deque.append(root)
        ans = []
        order_left = True
        while deque:
            level = collections.deque()
            for _ in range(len(deque)):
                node = deque.popleft()
                level.append(node.val) if order_left else level.appendleft(node.val)
                if node.left: deque.append(node.left)
                if node.right: deque.append(node.right)
            order_left = not order_left
            ans.append(list(level))
        return ans
# @lc code=end

