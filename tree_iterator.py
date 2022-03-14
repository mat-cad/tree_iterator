import logging
from abc import ABC, abstractmethod
from stack import Stack


class TreeIterator(ABC):
    def __init__(self, root):
        assert root is not None
        self._root = root
        self._is_there_a_next = True # the root

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def has_next(self):
        pass


class Preorder(TreeIterator):
    def __init__(self, root):
        super().__init__(root)
        self._current = self._root
        self._stack = Stack()

    def next(self):
        logging.debug('stack = {}'.format(self._stack))
        res = self._current
        if self._current.num_children > 0: # parent
            for i in range(1, self._current.num_children):
                self._stack.push(self._current.children[i])
            self._current = self._current.children[0]
        else: # leaf
            if not self._stack.is_empty():
                self._current = self._stack.pop()
            else:
                self._is_there_a_next = False
        return res

    def has_next(self):
        return self._is_there_a_next

#https://www.techiedelight.com/postorder-tree-traversal-iterative-recursive/
class Postorder(TreeIterator):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self._stack_in = Stack()
        self._stack_out = Stack()
        self._fill_stacks()

    def _fill_stacks(self):
        self._stack_in.push(self._root)
        while not self._stack_in.is_empty():
            logging.debug('stack_in = {}'.format(self._stack_in))
            logging.debug('stack_out = {}'.format(self._stack_out))
            current = self._stack_in.pop()
            self._stack_out.push(current)
            for i in range(current.num_children):
                self._stack_in.push(current.children[i])

    def next(self):
         return self._stack_out.pop()

    def has_next(self):
        return not self._stack_out.is_empty()