class Solution(object):
    def goodNodes(self, root):
        if root is None:
            return 0
        res = 0
        stack = [(root, root.val)]
        while stack:
            node, path_max = stack.pop()
            if node.val >= path_max:
                res += 1
            new_max = max(path_max, node.val)
            if node.right: stack.append((node.right, new_max))
            if node.left:  stack.append((node.left,  new_max))
        return res