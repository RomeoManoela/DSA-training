from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Breath First Search
def bfs(root: TreeNode) -> list[int]:
    result: list[int] = []
    queue: deque[TreeNode] = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


# Depht First Search
def preorder(root: TreeNode) -> list[int]:
    result: list[int] = []
    if not root:
        return result

    def helper(r: TreeNode) -> None:
        if r is None:
            return
        result.append(r.val)
        helper(r.left)
        helper(r.right)

    helper(root)
    return result


def postorder(root: TreeNode) -> list[int]:
    result: list[int] = []
    if root is None:
        return result

    def helper(r: TreeNode) -> None:
        if r is None:
            return
        helper(r.left)
        helper(r.right)
        result.append(r.val)

    helper(root)
    return result


def inorder(root: TreeNode) -> list[int]:
    result: list[int] = []
    if root is None:
        return result

    def helper(r: TreeNode) -> None:
        if r is None:
            return
        helper(r.left)
        result.append(r.val)
        helper(r.right)

    helper(root)
    return result
