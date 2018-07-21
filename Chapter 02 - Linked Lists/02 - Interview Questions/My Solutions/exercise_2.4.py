"""
@Student    Braulio Tonaco
@Date       07/21/18

2.4 Partition:
Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes
grater than or equal to x. If x is contained within the list, the values of x only need to be after the elements
less than x (see below). The partition element x can appear anywhere in the "right partition"; it does not need
to appear between the left and right partitions.

EXAMPLE:
    INPUT:  3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [ partition = 5]
    OUTPUT: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

"""
from Node import Node


def partition(head, n):
    before_head = None                  # Before pivot head
    before_tail = None                  # Before tail
    after_head = None                   # After pivot head
    after_tail = None                   # After pivot tail

    current = head

    while current is not None:
        nxt = current.next

        if current.data < n:
            if before_head is None:
                before_head = current
                before_tail = before_head
            else:
                before_tail.next = current
                before_tail = current
                before_tail.next = None  # In case all node are less than n
        else:
            if after_head is None:
                after_head = current
                after_tail = after_head
            else:
                after_tail.next = current
                after_tail = current
                after_tail.next = None  # Makes sure that tail points to None

        current = nxt

    if before_head is not None:
        before_tail.next = after_head


# ********** TEST CASE **********
input_list = [3, 5, 8, 5, 10, 2, 1]     # TEST DATA
head = Node(input_list[0])

for i in range(1, len(input_list)):     # Generate test Singly Linked List
    head.append_to_tail(input_list[i])

head.print_sequence()                   # OUTPUT: [3, 5, 8, 5, 10, 2, 1]

partition(head, 5)
head.print_sequence()                   # OUTPUT: [3, 2, 1, 5, 8, 5, 10]


