"""
@Student    Braulio Tonaco
@Date       07/23/18

2.8 Loop Detection:
Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop.

DEFINITION:
Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node,
so as to make a loop in the linked list.

EXAMPLE:
    INPUT: A -> B -> C -> D -> E -> C [ the same C as earlier ]
    OUTPUT: C

******************* PSEUDOCODE *******************
Lets use the runner method.
slow node will move 1 node at a time
fast node will move 2 nodes at a time

    set slow node equal to head
    set fast node equals to the second node after head

    while True
        if slow node is equal to fast node (found the first loop node)
            return slow or fast node

        if next node ahead fast node is not None
            set fast node equal next node

            if next node ahead of fast node is not None
                set fast node equal to next node
            otherwise linked list does not loop and return

        set current node equal to its next node

"""

from Node import Node


# ******************* TEST CASES *******************
# Linked List 1
A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')
G = Node('G')
H = Node('H')
I = Node('I')

A.next = B
B.next = C
C.next = D
D.next = E
E.next = F
F.next = G
G.next = E  # <- Starts loop
H.next = I


# ******************* SOLUTION *********************
def loop_detection(head):
    slow = head
    fast = head.next.next

    while True:
        if slow == fast:
            print 'Found Loop Node -> ' + slow.data
            return slow

        if fast.next is not None:
            fast = fast.next

            if fast.next is not None:
                fast = fast.next
            else:
                print 'Linked list does not loop'
                return
        slow = slow.next


# ******************* OUTPUT ***********************
loop_detection(A)  # OUTPUT: Found Loop Node -> E




