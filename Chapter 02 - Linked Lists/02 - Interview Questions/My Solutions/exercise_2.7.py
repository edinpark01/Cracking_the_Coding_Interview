"""
@Student    Braulio Tonaco
@Date       07/23/18

2.7 Intersection:
Given two (singly) linked lists, determine if the two lists intersect. Return the intersection node.

NOTE:
The intersection is defined based on reference, not value. That is, if the kth node of the first linked list
is the exact same node (by reference) as the jth node of the second linked list, they are intersection.

******************* PSEUDOCODE *******************

traverse first linked list
    for each node in the first linked list
        for each node on second linked list
            if first node is equal to second node
                return first node


        first node is equal to its next one

    state the fact that the two linked list does not intersect



"""

from Node import Node


# ******************* TEST CASES *******************
# LINKED LIST 1:    A -> B -> C -> D -> E -> F
# LINKED LIST 2:              G -> H -> E -> F
# In this example, linked list 1 & 2 intersect at the 5th node from list 1 and 3rt node from list 2

# Linked List 1
A = Node(0)
B = Node(1)
C = Node(2)
D = Node(3)
E = Node(4)
F = Node(5)
A.next = B
B.next = C
C.next = D
D.next = E
E.next = F

# Linked List 2
G = Node(0)
H = Node(1)
G.next = H
H.next = E


# ******************* SOLUTION *********************
def intersection(head1, head2):
    first = head1

    i = 1
    while first is not None:
        second = head2
        j = 1

        while second is not None:
            if first == second:
                print 'Intersection happens...'
                print '@ node ' + str(i) + ' from Linked List 1'
                print '@ node ' + str(j) + ' from Linked List 2'
                return first

            else:
                second = second.next
                j += 1

        first = first.next
        i += 1

    print "The two linked list do not intersect"
    return None


# ******************* OUTPUT ***********************
intersection(A, G)

# Intersection happens...
# @ node 5 from Linked List 1
# @ node 3 from Linked List 2






