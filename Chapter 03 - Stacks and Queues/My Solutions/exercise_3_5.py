"""
    @Student    Braulio Tonaco
    @Date       07/27/18

3.5 Sort Stack:
    Write a program to sort stack such that the smallest item are on the top. You can use an additional temporary stack,
but you may not copy the elements into any other data structure (such as an array). The stack supports the following
operation: PUSH, POP, PEEK, and ISEMPTY

PSEUDOCODE

PUSH
    while pushed data is > than stack head
        push head in temp stack

    push pushed data in main stack

    while temp stack is not empty
        push head in main stack

POP
    return main.pop

PEEK
    return main at last index

ISEMPTY
    return if length of main stack is empty


"""


class sort_stack:

    def __init__(self):
        self.main = []
        self.temp = []

    def push(self, data):
        if len(self.main) == 0:
            self.main.append(data)

        while not self.isEmpty() and data > self.peek():
            self.temp.append(self.main.pop())

        self.main.append(data)

        while len(self.temp) != 0:
            self.main.append(self.temp.pop())

    def pop(self):
        return self.main.pop()

    def isEmpty(self):
        return len(self.main) == 0

    def peek(self):
        if self.isEmpty():
            return None
        return self.main[-1]