"""
@Student    Braulio Tonaco
@Date       07/22/18

2.6 Palindrome:
Implement a function to check if a linked list is a palindrome

NOTE:
    We are assuming we can calculate the size of a linked list in advance
    With that:
        if a palindrome is even, first half must equal reverse of second half
        if a palindrome is odd, same as above BUT we skip the middle node

******************* PSEUDOCODE *******************

save head in a variable
initialize stack
initialize is a palindrome boolean to true

stack up first half of linked list

if linked list is odd skip middle node

while stack is not empty:
    pop top node and compare against current node

    if top node is not equal current node
        set is a palindrome boolean to false and exit loop

    current node equal next node


if is a palindrome boolean is true:
    confirm that linked list is a palindrome
otherwise:
    state the fact that linked list is not a palindrome

"""

from Node import Node

# ******************* TEST CASES *******************
cases = [
    ['A', 'B', 'C', 'B', 'A'],                  # EVEN palindrome
    ['A', 'B', 'C', 'B', 'C'],                  # EVEN non-palindrome
    ['A', 'B', 'C', 'D', 'D', 'C', 'B', 'A'],   # ODD palindrome
    ['A', 'B', 'C', 'D', 'D', 'C', 'B', 'B']    # ODD non-palindrome
]

head_nodes = []

for case in cases:
    head = None

    for data in case:
        if head is None:
            head = Node(data)
        else:
            head.append_to_tail( Node(data) )

    head_nodes.append(head)


# ******************* SOLUTION *******************
def palindrome(node):
    h = node
    is_palindrome = True
    stack = None
    n = node.get_size()

    for i in range(n / 2):                          # Stacks up first half nodes
        if stack is None:
            stack = [node]
        else:
            stack.append(node)

        node = node.next

    if n % 2 != 0:                                  # If linked list size is odd, skip middle node
        node = node.next

    while len(stack) != 0:                          # Crosscheck first half against second half
        if stack.pop().data != node.data:
            is_palindrome = False
            break
        node = node.next

    if is_palindrome:                               # Display results
        h.print_sequence()
        print 'Linked List is a Palindrome\n'
    else:
        h.print_sequence()
        print 'Linked List is not a Palindrome\n'


for head in head_nodes:
    palindrome(head)


# ******************* OUTPUT *******************
#
# ['A', 'B', 'C', 'B', 'A']
# Linked List is a Palindrome
#
# ['A', 'B', 'C', 'B', 'C']
# Linked List is not a Palindrome
#
# ['A', 'B', 'C', 'D', 'D', 'C', 'B', 'A']
# Linked List is a Palindrome
#
# ['A', 'B', 'C', 'D', 'D', 'C', 'B', 'B']
# Linked List is not a Palindrome





