"""
    BINARY TREE TRAVERSAL
    Your should be comfortable implementing in-order, post-order, and pre-order traversal. The most common of
these is in-order traversal.


    IN-ORDER TRAVERSAL
    In-order traversal means to "visit" (often-print) the left branch, then the current node, and finally,
the right branch.

    PRE-ORDER TRAVERSAL
    Pre-order traversal visits the current node before its child nodes (hence the name "pre-order")


    POST-ORDER TRAVERSAL
    Post-order traversal visits the current node after its child nodes (hence the name "post-order")
"""


def in_order_traversal(node):
    # When performed on a binary search tree, in-order traversal visits nodes in ascending order
    # (hence the name "in-order")
    if node is not None:
        in_order_traversal(node.left)   # "visit" left node
        print node                      # "visit" current node
        in_order_traversal(node.right)  # "visit" right node


def pre_order_traversal(node):
    # In pre-order traversal, the root is always to first node to be visited
    if node is not None:
        print node                      # "visit" current node
        in_order_traversal(node.left)   # "visit" left node
        in_order_traversal(node.right)  # "visit" right node


def post_order_traversal(node):
    # In post-order traversal, the root is always to last node to be visited
    if node is not None:
        in_order_traversal(node.left)   # "visit" left node
        in_order_traversal(node.right)  # "visit" right node
        print node                      # "visit" current node
