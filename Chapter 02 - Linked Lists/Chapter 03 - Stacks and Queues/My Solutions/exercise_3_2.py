"""
    @Student    Braulio Tonaco
    @Date       07/24/18

    3.2 Stack Min:
        How would you design a stack which, in addition to push and pop, has a function min which returns
    the minimum element? Push, pop and min should all operate in O(1)

"""
import sys


class Stack:  # Using simple doubly linked list implementation

    def __init__(self):
        self.main = []                          # main stack
        self.min_stack = []                     # stack to store min values

    def push(self, data):
        if data <= self.min():
            self.min_stack.append(data)
        self.main.append(data)

    def pop(self):
        if self.isEmpty():
            raise ValueError("Stack is empty")

        value = self.main.pop()

        if value == self.min():
            return self.min_stack.pop()

        return value

    def min(self):
        if self.isEmpty():
            return sys.maxint  # ERROR
        else:
            return self.min_stack[-1]  # Peek

    def isEmpty(self):
        return len(self.min_stack) == 0
