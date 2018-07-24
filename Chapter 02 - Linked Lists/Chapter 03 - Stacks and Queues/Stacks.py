"""
IMPLEMENTING THE STACK

    The stack data structure is precisely what it sounds like: a stack of data. In certain types of problems, it can
be favorable to store data in a stack rather than in an array.
    A stacks uses LIFO (last-in first-out) ordering. That is, as in a stack of dinner plates, the ost recent item
added to the stack is the first item to be removed.

    It uses the following operations:
    - pop()         remove the top item from the stack
    - push(item)    add an item to the top of the stack
    - peek()        return the top of the stack
    - isEmpty()     Return true if and only if the stack is empty

    Unlike an array, a stack does not offer constant-time access to the ith item. However, it does allow constant time
adds and removes, as it does not require shifting elements around.
    We have provided simple sample code to implement a stack. Note that a stack can also be implemented using a
linked list, if items were added and removed from the same side.

"""


class Node:  # We are going to use a simple Node class from chapter 2

    def __init__(self, d):
        self.data = d
        self.next = None


class Stack:  # Simple implementation

    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            temp = self.head  # saves current head in a temporary variable
            self.head = Node(data)  # sets new top node
            self.head.next = temp  # new head now refers to older head as its next node

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
    One case where stacks are often useful is in certain recursive algorithms. Sometimes you need to push temporary
data onto a stack as you recurse, but then remove them as you backtrack (for example, because the recursive 
check failed). A stack offers an intuitive way to do this. 

"""