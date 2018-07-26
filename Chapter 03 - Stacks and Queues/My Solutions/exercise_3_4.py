"""
    @Student    Braulio Tonaco
    @Date       07/25/18

3.4 Queue via Stacks:
    Implement a MyQueue class which implements a queue using two stacks

"""


class MyQueue:

    def __init__(self):
        self.new_stack = []
        self.old_stack = []

    def add(self, data):
        self.new_stack.append(data)

    def remove(self):
        if self.isEmpty():
            raise ValueError("Queue is empty")

        self.dump()

        return self.old_stack.pop()

    def peek(self):
        if self.isEmpty():
            return None

        self.dump()

        return self.old_stack[-1]

    def isEmpty(self):
        return len(self.old_stack) == 0 and len(self.new_stack) == 0

    def dump(self):
        if len(self.old_stack) == 0:
            while len(self.new_stack) != 0:
                self.old_stack.append(self.new_stack.pop())