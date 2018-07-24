"""
IMPLEMENTING A QUEUE

    A queue implements FIFO (first-in first-out) ordering. As in a line or queue at a ticket stand, items are
removed from the data structure in the same order that they are added.

    It uses the operations:
    - add(item)     Add an item to the end of the list
    - remove()      Remove the first item in the list
    - peek()        Return the top of the queue
    - isEmpty()     Return true if and only if the queue is empty

    A queue can also be implemented with a linked list. In fact, they are essentially the same thing,
as long as items are added and removed from opposite sides
"""


class Node:  # We are going to use a simple Node class from chapter 2
    def __init__(self, d):
        self.data = d
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            temp = self.tail        # saves current tail in a temporary variable
            self.tail = Node(data)  # sets new tail node
            temp.next = self.tail   # old tail now refers to new tail as its next node

    def pop(self):
        if self.head is None:
            raise ValueError("Can not use pop() method, stack is empty!")
        data = self.head.data
        self.head = self.head.next
        return data

    def peek(self):
        if self.head is None:
            raise ValueError("Can not use peek() method, stack is empty!")
        return self.head.data

    def isEmpty(self):
        return self.head is None
"""
    It is specially easy to mess up the updating of the first and last nodes in a queue. Be sure to double check this
    One place where queues are often used is in breadth-first search or implementing cache.
    In breadth-first-search, for example, we used a queue to store a list of the nodes that we need to process. 
Each time we process a node, we add its adjacent nodes to the back of the queue. This allows us to process nodes in the 
order in which they are viewed.

"""
