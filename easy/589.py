class TreeNode:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children else []


class Solution:
    def preorderTraversal(self, root):
        result = []

        def preorder(node):
            if node is None:
                return
            result.append(node.val)
            for child in node.children:
                preorder(child)

        preorder(root)
        return result


root = TreeNode(1, [
    TreeNode(3, [TreeNode(5), TreeNode(6)]),
    TreeNode(2),
    TreeNode(4)
])

s = Solution()
print(s.preorderTraversal(root))