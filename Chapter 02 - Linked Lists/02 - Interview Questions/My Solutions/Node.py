class Node:

    def __init__(self, data):
        self.data = data
        self.next = None  # the pointer initially points to nothing

    def append_to_tail(self, end):
        n = self

        while n.next is not None:
            n = n.next

        n.next = end

    def remove_dup_with_buffer(self):
        current = self
        previous = None
        tracker = {}

        while current is not None:
            if current.data not in tracker:
                tracker[current.data] = 'New Unique Node'
                previous = current
            else:
                previous.next = current.next

            current = current.next

    def remove_dup_without_buffer(self):
        current = self

        while current is not None:
            runner = current

            while runner.next is not None:  # remove all future nodes w/ same data
                if runner.next.data == current.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next

            current = current.next

    def get_size(self):
        counter = 0
        n = self

        while n is not None:
            counter += 1
            n = n.next

        return counter

    def print_sequence(self):
        n = self
        lst = []

        while n is not None:
            lst.append(n.data)
            n = n.next

        print lst