"""
    @Student    Braulio Tonaco
    @Date       07/25/18

3.3 Stack of plates:
    Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore, in real life, we
would likely start a new stack when the previous stack exceeds some threshold. Implement a data structure
SetOfStacks that mimics this. Set of Stacks should be composed of several stacks and should create a new stack once the
previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack
( that is, pop() should return the same values as it would if there were just a single stack).

FOLLOW UP
    Implement a function popAt(int index) which performs a pop operation on a specific sub-stack.

"""

class SetOfStacks:

    def __init__(self):
        self.stack_size = 5
        self.stacks = []

    def push(self, data):
        if len(self.stacks) == 0:
            self.stacks.append([data])
        elif len(self.stacks[-1]) == self.stack_size:
            self.stacks.append([data])
        else:
            self.stacks[-1].append(data)

    def pop(self):
        if self.isEmpty():
            raise ValueError("Stack is empty")
        elif len(self.stacks[-1]) == 0:
            self.stacks.pop()
            return self.pop()  # Recursive call
        else:
            temp = self.stacks[-1].pop()
            return temp

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.stacks[-1][-1]

    def isEmpty(self):
        return len(self.stacks) == 0

# FOLLOW UP QUESTION
    def popAt(self, index):
        if self.isEmpty():
            raise ValueError("Stack is empty")

        if index > self.stackSize():
            raise ValueError("Index {} out of bounds".format(index))

        pile = index / self.stack_size
        sub_idx = index % self.stack_size
        n = len(self.stacks) - pile - 1

        data = self.stacks[pile].pop(sub_idx)

        self.shift_left(pile, n)

        return data

    def stackSize(self):
        return (len(self.stacks) * self.stack_size) - (5 - len(self.stacks[-1]))

    def shift_left(self, pile, n):
        if n == 0 or len(self.stacks[pile + 1]) == 0:
            return
        self.stacks[pile].append(self.stacks[pile + 1].pop(0))
        return self.shift_left(pile + 1, n - 1)