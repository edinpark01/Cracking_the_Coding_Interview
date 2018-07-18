"""
A linked list is a linear data structure where each element is a separate object.

Each element or node of a list is comprising of two items:
    * Data
    * Reference to the next node

The last node has a referent to null. The entry point into a linked list is called the head of the list. It should
be noted that the head is not a separate node, but the reference to the first node. If the list is empty then
the head is a null reference.

ADVANTAGES
Linked list nodes can live anywhere in the memory. Whereas an array requires a sequence of memory to be initiated,
as long as the reference are updated, each linked list node can be flexibly moved to a different address.

DISADVANTAGES
Unlike an array, a linked list does not provide constant time access to a particular "index" within the list.
If you want to access a particular node at the Kth element you will have to iterate through K nodes.

TYPES OF LINKED LISTS
1. Singly linked list: describe above
2. Doubly linked list: is a list that has two references, one to the next node and another to the previous node.

If multiple objects need a reference to the linked list, and then the head of the linked list changes some
objects might still be pointing to the old head
"""

# Creating a Linked List
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None  # the pointer initially points to nothing

    def append_to_tail(self, data):
        end = Node(data)
        n = self

        while (n.next != None):
            n = n.next

        n.next = end


# DELETING A NODE FROM A SINGLY LINKED LIST
#
# Deleting a node from a linked list is fairly straightforward. Given a node n:
#
# STEP 1: Traverse linked list to find node n, saving at each iteration its previous node
# STEP 2: Set previous_node.next = n.next
#
# If the list is doubly linked...
# STEP 1: Update n.next
# STEP 2: Set n.next.prev = n.prev
#
# The important things to remember are:
#     1.  To check for the null pointer
#     2.  To update the head or tail pointer as necessary
#
# Additionally, if you implement this code in C, C++ or another language that requires the developer to do
# memory management, you should consider if the removed node should be dealocated.

    def delete_node(self, head, data):
        n = head

        # move head
        if n.data == data:
            return head.next

        # traverse linked list
        while n.next is not None:

            # head did not change
            if n.next.data == data:
                n.next = n.next.next
                return head

            n = n.next

        return head
"""
THE "RUNNER" TECHNIQUE

    The "runner" (or second pointer) technique is used in many linked list problems. The runner technique
means that you iterate through the linked list with two pointers simultaneously, with one ahead of the
other. The "fast" node might be ahead by a fixed amount, or it might be hopping multiple nodes for each one 
node that the "slow" node iterates through.

EXAMPLE:
Suppose you had a linked list:

                        a1 -> a2 -> a3 -> ... -> an -> b1 -> b2 -> ... -> bn
                        
and you wanted to rearrange it into: 
                    
                        a1 -> b1 -> a2 -> b2 -> a3 -> b4 -> ... -> an -> bn
                        
    You do not know the length of the linked list (but you do know that the length is an even number). 
You could have one pointer p1 (the fast pointer) move every two elements for every one move that p2 makes. 
When p1 hits the end of the linked list, p2 will be at the midpoint. Then, move p1 back to the front and begin 
"weaving" the elements. On each iteration, p2 selects an element and inserts it after p1. 

RECURSIVE PROBLEMS

    A number of linked list problems rely on recursion. If you are having trouble solving a linked list problem, 
you should explore if a recursive approach will work. We won't go into depth on recursion here, since a later chapter 
is devoted to it. 
    However, you should remember that recursive algorithms take at least O(n) space, where n is the depth of the 
recursive call. All recursive algorithms can be implemented iteratively, although they may be much more complex.

"""
