"""
@Student    Braulio Tonaco
@Date       07/19/18

2.2 Return the Kth to Last:
Implement an algorithm to find the kth to last element of a singly linked list.

"""

from random import randint as r
from Node import Node


def find_nth_node(k, head):
    p1 = head  # Faster pointer (Runner)
    p2 = head  # Slower pointer

    # Move runner k times into the linked list
    for j in range(k):
        if p1 is None:
            return None  # Out of bounds
        p1 = p1.next

    # Move
    while p1 is not None:
        p1 = p1.next
        p2 = p2.next

    print p2.data


# Initialize test case
n = 10
k = 5
first_node = Node(4)

for i in range(n):
    first_node.append_to_tail(r(0, 99))

find_nth_node(k, first_node)

"""
[4, 60, 59, 69, 25, 8, 37, 83, 19, 53] -> Linked list
                      [37]             -> Returned node

EXPLANATION:
    We can use two pointer, p1 and p2. We place them k nodes apart in the linked list by putting p2 at the 
beginning and moving p1 k nodes into the list. Then, when we move them at the same pace, p1 will hit the end 
of the linked list after LENGTH - k steps. At that point, p2 will be LENGTH - k nodes into the list, 
or k nodes from the end. 
"""