"""
    @Student    Braulio Tonaco
    @Date       07/24/18

    3.1 Three in One:
        Describe how you could use a single array to implement three stacks.


"""


class Stack:  # Simple implementation using a list

    def __init__(self, size):
        self.size = size
        self.stack = [0 for i in range(size)]

        self.limit1 = self.size / 3
        self.limit2 = self.size * 2 / 3
        self.limit3 = self.size

        self.head1 = -1
        self.head2 = self.size / 3 - 1
        self.head3 = self.size * 2 / 3 - 1

    def push(self, data, s):
        if s == 1:
            self.head1 += 1

            if self.head1 == self.limit1:
                raise ValueError('Stack 1 exceeded its size')

            self.stack[self.head1] = data
        elif s == 2:
            self.head2 += 1

            if self.head2 == self.limit2:
                raise ValueError('Stack 2 exceeded its size')

            self.stack[self.head2] = data
        elif s == 3:
            self.head3 += 1

            if self.head3 == self.limit3:
                raise ValueError('Stack 3 exceeded its size')

            self.stack[self.head3] = data

    def pop(self, s):
        if s == 1:
            if self.head1 == -1:
                raise ValueError('Stack 1 is empty')

            self.head1 -= 1
            return self.stack[self.head1]
        elif s == 2:
            if self.head2 == self.limit1:
                raise ValueError('Stack 2 is empty')

            self.head2 -= 1
            return self.stack[self.head2]
        elif s == 3:
            if self.head3 == self.limit2:
                raise ValueError('Stack 1 is empty')

            self.head3 -= 1
            return self.stack[self.head3]

    def peek(self, s):
        if s == 1:
            if self.head1 == -1:
                raise ValueError('Stack 1 is empty')
            return self.stack[self.head1]
        elif s == 2:
            if self.head2 == self.limit1:
                raise ValueError('Stack 2 is empty')
            return self.stack[self.head2]
        elif s == 3:
            if self.head3 == self.limit2:
                raise ValueError('Stack 1 is empty')
            return self.stack[self.head3]

    def isEmpty(self, s):
        if s == 1:
            return self.head1 == -1
        elif s == 2:
            return self.head2 == self.limit1 - 1
        elif s == 3:
            return self.head3 == self.limit2 - 1


"""
BOOK OVERVIEW

    Like many problems, this one somewhat depends on how well we'd like to support these stacks. If we are
okay with simply allocating a fixed amount of space for each stack, we can do that. 
This may mean though the one stack runs out of space, while the others are nearly empty. 

Our approach: Fixed Division
    We can divide the array in three equal parts and allow the individual stack to grow in that limited space. 

"""