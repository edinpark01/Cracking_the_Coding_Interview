"""
@Student    Braulio Tonaco
@Date       07/18/18

2.1 Remove Dups:
    A) Write code to remove duplicates from an unsorted linked list
    B) How would you solve this problem if a temporary buffer is not allowed?
"""
from Node import Node
from random import randint as r


def remove_dup_with_buffer(head):
    """ A) Write code to remove duplicates from an unsorted linked list """
    current = head
    previous = None
    tracker = {}

    while current is not None:
        if current.data not in tracker:
            tracker[current.data] = 'New Unique Node'
            previous = current
        else:
            previous.next = current.next

        current = current.next


def remove_dup_without_buffer(head):
    """ B) How would you solve this problem if a temporary buffer is not allowed? """
    current = head

    while current is not None:
        runner = current

        while runner.next is not None:  # remove all future nodes w/ same data
            if runner.next.data == current.data:
                runner.next = runner.next.next
            else:
                runner = runner.next

        current = current.next


# Generate test cases
head1 = Node(1)
for i in range(2000):
    head1.append_to_tail(r(0, 10))
head2 = Node(1)
for i in range(2000):
    head2.append_to_tail(r(0, 10))

# ****************** SOLUTION FOR A ******************
print head1.get_size()  # OUTPUT: 2000
remove_dup_with_buffer(head1)
print head1.get_size()  # OUTPUT: 10

# ****************** SOLUTION FOR B ******************
print head2.get_size()  # OUTPUT: 2000
remove_dup_without_buffer(head2)
print head2.get_size()  # OUTPUT: 10
