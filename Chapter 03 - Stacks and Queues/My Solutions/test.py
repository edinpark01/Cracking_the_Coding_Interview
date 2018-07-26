from exercise_3_4 import MyQueue

queue = MyQueue()

for i in range(10):
    queue.add(i)

print queue.peek()

for j in range(10):
    print queue.remove()