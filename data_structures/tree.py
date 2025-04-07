from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Tree Traversal
def recur_inorder(node):
    res = []
    if node is None: return res
    res += recur_inorder(node.left)
    res += [node.val]
    res += recur_inorder(node.right)
    return res

def recur_preorder(node):
    res = []
    if node is None: return res
    res += [node.val]
    res += recur_preorder(node.left)
    res += recur_preorder(node.right)
    return res

def recur_postorder(node):
    res = []
    if node is None: return res
    res += recur_postorder(node.left)
    res += recur_postorder(node.right)
    res += [node.val]
    return res

def level_order(node):
    q = deque([node])
    res = []
    while q:
        level = len(q)
        for _ in range(level):
            c = q.popleft()
            res.append(c.val)
            if c.left: q.append(c.left)
            if c.right: q.append(c.right)
    return res

def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    # [1, 2, 3, 4, 5, 6, 7]

    print(recur_inorder(root))
    print(recur_preorder(root))
    print(recur_postorder(root))
    print(level_order(root))

if __name__ == '__main__':
    main()