"""
@Student    Braulio Tonaco
@Date       07/21/18

2.5 Sum Lists:
a)  You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored
    in reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers
    and returns the sum as a linked list.

EXAMPLE:
    INPUT: ( 7 -> 1 -> 6 ) + ( 5 -> 9 -> 2 ). That is, 617 + 295
    OUTPUT: 2 -> 1 -> 9

b)  Suppose the digits are store in forward order. Repeat the above problem.

EXAMPLE:
    INPUT: ( 6 -> 1 -> 7 -> 8 ) + ( 2 -> 9 -> 5 ). That is, 617 + 295
    OUTPUT: 9 -> 1 -> 2

"""
from Node import Node


def padding(s1, s2):
    padding_node = None

    while s1 < s2:
        if padding_node is None:
            padding_node = Node(0)
        else:
            padding_node.append_to_tail(Node(0))
        s1 += 1

    return padding_node


def forward_recursive_sum(l1, l2, previous, size1=0, size2=0):
    if l1 is None and l2 is None:
        return None

    # Adds zero for smaller linked list
    if size1 > size2:
        pad_node = padding(size2, size1)
        pad_node.append_to_tail(l2)
        l2 = pad_node
    elif size1 < size2:
        pad_node = padding(size1, size2)
        pad_node.append_to_tail(l1)
        l1 = pad_node

    value = l1.data + l2.data

    if value >= 10 and previous is not None:
        previous.data += 1

    current = Node(value % 10)

    next1 = None if l1.next is None else l1.next
    next2 = None if l2.next is None else l2.next

    # Recursive call
    current.next = forward_recursive_sum(next1, next2, current)

    return current


def reverse_recursive_sum(l1, l2, carry):
    if l1 is None and l2 is None and carry == 0:
        return None

    value = carry

    if l1 is not None:
        value += l1.data
    if l2 is not None:
        value += l2.data

    node = Node(value % 10)

    if l1 is not None or l2 is not None:
        l1 = None if l1 is None else l1.next
        l2 = None if l2 is None else l2.next
        carry = 0 if value < 10 else 1

        more = reverse_recursive_sum(l1, l2, carry)

        node.next = more

    return node


# **************** Exercise 2.5 - a ****************
n1 = None
n1_digits = [7, 1, 6]

n2 = None
n2_digits = [5, 9, 2]

# Initialize both linked lists
for i, j in zip(n1_digits, n2_digits):
    if n1 is None and n2 is None:
        n1 = Node(i)
        n2 = Node(j)
    else:
        n1.append_to_tail(Node(i))
        n2.append_to_tail(Node(j))

n3 = reverse_recursive_sum(n1, n2, 0)

n1.print_sequence()  # OUTPUT: [7, 1, 6]
n2.print_sequence()  # OUTPUT: [5, 9, 2]
n3.print_sequence()  # OUTPUT: [2, 1, 9]


# **************** Exercise 2.5 - a ****************
n1 = None
n1_digits = [6, 1, 7, 8]

n2 = None
n2_digits = [2, 9, 5]

# Initialize both linked lists
for i in n1_digits:
    if n1 is None:
        n1 = Node(i)
    else:
        n1.append_to_tail(Node(i))

for j in n2_digits:
    if n2 is None:
        n2 = Node(j)
    else:
        n2.append_to_tail(Node(j))


n3 = forward_recursive_sum(n1, n2, None, n1.get_size(), n2.get_size())

n1.print_sequence()  # OUTPUT: [6, 1, 7, 8]
n2.print_sequence()  # OUTPUT: [2, 9, 5]
n3.print_sequence()  # OUTPUT: [6, 4, 7, 3]
