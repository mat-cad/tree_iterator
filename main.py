import logging
from tree import Parent, Leaf
from tree_iterator import Preorder, Postorder

logging.getLogger().setLevel(logging.DEBUG)


"""
A decision tree, parents have a pair (k,v) and leaves a label
    root(0,1.)
    /   \
   /     \
p1(1,2.) l3(c)
   / \
  /   \
l1(a)  l2(b)  
"""
root = Parent(0, 1.0)
p1 = Parent(1, 2.0)
l1 = Leaf("a")
l2 = Leaf("b")
l3 = Leaf("c")
p1.add_children(l1,l2)
root.add_children(p1, l3)

for iter in [Preorder(root), Postorder(root)]:
    while iter.has_next():
        node = iter.next()
        logging.debug(node)
        print(node)
    print('---------')