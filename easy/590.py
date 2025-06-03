class TreeNode:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children else []


class Solution:
    def preorderTraversal(self, root):
        result = []

        def postorder(node):
            if node is None:
                return
            for child in node.children:
                postorder(child)
            result.append(node.val)

        postorder(root)
        return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(6)
root.left.right.right = TreeNode(7)
root.right.right = TreeNode(8)
root.right.right.left = TreeNode(9)

s = Solution()
print(s.preorderTraversal(root))