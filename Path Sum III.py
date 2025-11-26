class Solution(object):
    def pathSum(self, root, targetSum):
        if not root:
            return 0
        num = [0]

        def currentPath(node, path, currentSum):
            if not node:
                return
            currentSum += node.val
            if currentSum == targetSum:
                num[0] += 1
            currentPath(node.left, path + [node.val], currentSum)
            currentPath(node.right, path + [node.val], currentSum)

        def dfs(node):
            if not node:
                return
            currentPath(node, [], 0)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return num[0]