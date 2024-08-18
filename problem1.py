import sys, threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self):
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self.result = []

        def InOrderTraversal(tree):
            if tree == -1:
                return
            InOrderTraversal(self.left[tree])
            self.result.append(self.key[tree])
            InOrderTraversal(self.right[tree])

        InOrderTraversal(0)

        return self.result

    def preOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        def PreOrderTraversal(tree):
            if tree == -1:
                return
            self.result.append(self.key[tree])
            PreOrderTraversal(self.left[tree])
            PreOrderTraversal(self.right[tree])

        PreOrderTraversal(0)

        return self.result

    def postOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        def PostOrderTraversal(tree):
            if tree == -1:
                return
            PostOrderTraversal(self.left[tree])
            PostOrderTraversal(self.right[tree])
            self.result.append(self.key[tree])

        PostOrderTraversal(0)

        return self.result


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()
