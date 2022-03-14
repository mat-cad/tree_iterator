# A stack is already implemented in the Collections package, through
# the deque() factory. A deque has pop() and an append() instead of push().
# You can get a stack with
#   from collections import dequeue
#   stack = deque()
# This class is provided for completeness
class Stack:
    def __init__(self):
        self._stack = []

    def push(self, node): # add to the end
        self._stack.append(node)

    def pop(self): # remove from the end
        pop = self._stack[-1] # last
        self._stack = self._stack[:-1]  # remove last
        return pop

    def is_empty(self):
        return len(self._stack) == 0

    def __str__(self):
        return str([str(node) for node in self._stack])