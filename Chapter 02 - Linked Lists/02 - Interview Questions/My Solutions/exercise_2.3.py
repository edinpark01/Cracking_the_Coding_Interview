"""
@Student    Braulio Tonaco
@Date       07/21/18

2.3 Delete Middle Node:
Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node, not necessarily
the exact middle) of a singly linked list, give only access to that node.

EXAMPLE:
    INPUT: The node c from the linked list [ a -> b -> c -> d -> e -> f ]
    RESULT: Nothing is returned, but the new linked list looks like [ a -> b -> d -> e -> f ]

"""

from Node import Node


def delete_middle(current):

    if current is None or current.next is None:
        print "Cant delete node {}, its the last one in SinglyLinked List".format(current.data)
        return

    next_data = current.next.data
    next_next = current.next.next

    current.data = next_data
    current.next = next_next


A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')
G = Node('G')

A.next = B
B.next = C
C.next = D
D.next = E
E.next = F
F.next = G

A.print_sequence()      # OUTPUT: ['A', 'B', 'C', 'D', 'E', 'F', 'G']

delete_middle(C)
A.print_sequence()      # OUTPUT: ['A', 'B', 'D', 'E', 'F', 'G']

delete_middle(G)        # OUTPUT: Cant delete node G, its the last one in SinglyLinked List

"""
EXPLANATION:

In this problem, you are not given access to the head of the linked list. You only have access to that node.
The solution is simply to copy the data from the next node over the curren node, and then to delete the next node

"""


