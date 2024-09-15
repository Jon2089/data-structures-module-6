import sys

class Vertex:
    def __init__(self, key, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent
        self.size = 1

def update(v):
    if v is None:
        return
    v.size = 1 + (v.left.size if v.left is not None else 0) + (v.right.size if v.right is not None else 0)
    if v.left is not None:
        v.left.parent = v
    if v.right is not None:
        v.right.parent = v

def smallRotation(v):
    parent = v.parent
    if parent is None:
        return
    grandparent = parent.parent
    if parent.left == v:
        m = v.right
        v.right = parent
        parent.left = m
    else:
        m = v.left
        v.left = parent
        parent.right = m
    update(parent)
    update(v)
    v.parent = grandparent
    if grandparent is not None:
        if grandparent.left == parent:
            grandparent.left = v
        else:
            grandparent.right = v

def bigRotation(v):
    if v.parent.left == v and v.parent.parent.left == v.parent:
        smallRotation(v.parent)
        smallRotation(v)
    elif v.parent.right == v and v.parent.parent.right == v.parent:
        smallRotation(v.parent)
        smallRotation(v)    
    else:
        smallRotation(v)
        smallRotation(v)

def splay(v):
    if v is None:
        return None
    while v.parent is not None:
        if v.parent.parent is None:
            smallRotation(v)
            break
        bigRotation(v)
    return v

def find(root, index):
    current_node = root
    last = None

    if current_node is None or index >= current_node.size:
        return (None, root)
    
    while True:
        left_size = current_node.left.size if current_node.left is not None else 0
        
        if index == left_size:
            root = splay(last)
            return (current_node, root)
        
        last = current_node
        
        if index < left_size:
            current_node = current_node.left
        else:
            index -= (left_size + 1)
            current_node = current_node.right

def split(root, key):
    (result, root) = find(root, key)
    if result is None:
        return (root, None)
    right = splay(result)
    left = right.left
    right.left = None
    if left is not None:
        left.parent = None
    update(left)
    update(right)
    return (left, right)

def merge(left, right):
    if left is None:
        return right
    if right is None:
        return left
    while right.left is not None:
        right = right.left
    right = splay(right)
    right.left = left
    update(right)
    return right

def construct_tree(s):
    def build_subtree(l, r, parent=None):
        if l > r:
            return None
        
        if l == r:
            return Vertex(key=s[l], parent=parent)
        
        mid = (l + r) // 2
        left_child = build_subtree(l, mid - 1, parent)
        right_child = build_subtree(mid + 1, r, parent)
        
        root = Vertex(key=s[mid], left=left_child, right=right_child, parent=parent)
        update(root)
        
        return root
    
    return build_subtree(0, len(s) - 1)

def tree_to_string(root):
    def in_order_traversal(node):
        if node is None:
            return ''
        return in_order_traversal(node.left) + node.key + in_order_traversal(node.right)
    
    return in_order_traversal(root)

class Rope:
    def __init__(self, s):
        self.root = construct_tree(s)
    
    def result(self):
        return tree_to_string(self.root)
    
    def process(self, i, j, k):
        left, middle = split(self.root, i)
        middle, right = split(middle, j - i + 1)
        left_right = merge(left, right)
        left, right = split(left_right, k)
        self.root = merge(merge(left, middle), right)
        return self.result()

rope = Rope(sys.stdin.readline().strip())
q = int(sys.stdin.readline())
for _ in range(q):
    i, j, k = map(int, sys.stdin.readline().strip().split())
    rope.process(i, j, k)
print(rope.result())

