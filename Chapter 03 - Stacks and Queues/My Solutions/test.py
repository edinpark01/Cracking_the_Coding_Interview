from exercise_3_6 import AnimalShelter

stack = AnimalShelter()

stack.enqueue('CAT')
stack.enqueue('CAT')
stack.enqueue('CAT')
stack.enqueue('DOG')
stack.enqueue('CAT')
stack.enqueue('CAT')
stack.enqueue('DOG')
stack.enqueue('CAT')
stack.enqueue('CAT')
stack.enqueue('DOG')
stack.enqueue('DOG')
stack.enqueue('DOG')
stack.enqueue('DOG')
stack.enqueue('DOG')
stack.enqueue('CAT')

print stack.dequeueCAT()
print stack.dequeueCAT()
print stack.dequeueCAT()
print stack.dequeueDOG()
print stack.dequeueDOG()
print stack.dequeueDOG()
print stack.dequeueDOG()

print '\nRemaining...\n'

while not stack.isEmpty():
    print stack.dequeueANY()