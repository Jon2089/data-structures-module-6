# python3

import sys

class Rope:
    def __init__(self, s):
        self.s = s

    def result(self):
        return self.s

    def process(self, i, j, k):
        # Step 1: Cut substring S[i:j+1]
        substring = self.s[i:j+1]
        # Step 2: Remove the substring from original string
        self.s = self.s[:i] + self.s[j+1:]
        # Step 3: Insert the substring after the k-th symbol
        self.s = self.s[:k] + substring + self.s[k:]

# Reading input
rope = Rope(sys.stdin.readline().strip())
q = int(sys.stdin.readline())
for _ in range(q):
    i, j, k = map(int, sys.stdin.readline().strip().split())
    rope.process(i, j, k)

# Output result
print(rope.result())

