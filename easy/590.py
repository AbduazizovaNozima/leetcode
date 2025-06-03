class TreeNode:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children else []


class Solution:
    def postorderTraversal(self, root):
        result = []

        def postorder(node):
            if node is None:
                return
            for child in node.children:
                postorder(child)
            result.append(node.val)

        postorder(root)
        return result


root = TreeNode(1, [
    TreeNode(3, [TreeNode(5), TreeNode(6)]),
    TreeNode(2),
    TreeNode(4)
])

s = Solution()
print(s.postorderTraversal(root))