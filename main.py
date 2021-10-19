# Solution 1 - Recursively
# O(n) time | O(h) space, where n is the number of nodes in the Binary Tree
# h is the the height of the Binary Tree
def nodeDepths(root, depth = 0):
    '''
    The distance between a node in a Binary Tree and the tree's root is called the node's depth.
    Write a function that takes in a Binary Tree and returns the sum of its nodes' depths.
    Each BinaryTree node has an integer value, a left child node, and a right child node.
    Children nodes can either be Binary Tree nodes themselves or None / null,
    '''
    if root is None:
        return 0
    return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)

# Solution 2 - Iteratively
# O(n) time | O(h) space, where n is the number of nodes in the Binary Tree
# h is the the height of the Binary Tree
def nodeDepths1(root):
    sum_of_depth = 0
    call_stack = [{"node": root, "depth": 0}]
    while len(call_stack) > 0:
        node_info = call_stack.pop()
        node, depth = node_info['node'], node_info['depth']
        if node is None:
            continue
        sum_of_depth += depth
        call_stack.append({"node": node.left, "depth": depth + 1})
        call_stack.append({"node": node.right, "depth": depth + 1})
    return sum_of_depth

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
