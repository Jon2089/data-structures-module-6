import sys, threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 25)  # new thread will get stack of such size


def IsBinarySearchTree(tree):
    # Implement correct algorithm here
    if not tree:
        return True

    stack = [(0, -float('inf'), float('inf'))]

    while stack:
        node, min_val, max_val = stack.pop()

        if node == -1:
            continue

        value, left, right = tree[node]

        if not min_val < value < max_val:
            return False

        stack.append((right, value, max_val))
        stack.append((left, min_val, value))

    return True


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
