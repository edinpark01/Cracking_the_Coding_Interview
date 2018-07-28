"""
    @Student    Braulio Tonaco
    @Date       07/27/18

3.6 Animal Shelter:
    An animal shelter, which holds only dogs and cats, operates on a strictly "FIFO" basis. People must adopt either
the oldest (based on arrival time) of all animals at the shelter, or they can select whether they would prefer a dog or
a cat (and will receive the oldest animal of that type). They cannot select which specific animal they would like.
Create the data structures to maintain this system and implement operations such as enqueue, dequeueANY, dequeueDOG, and
dequeueCAT. You may use the built-in LinkedList data structure.

"""

class AnimalShelter:

    def __init__(self):
        self.main = []
        self.temp = []

    def enqueue(self, animal):
        self.main.append(animal)

    def dequeueANY(self):
        if self.isEmpty():
            raise ValueError("No animals in shelter!")
        else:
            return self.main.pop(0)

    def dequeueDOG(self):
        if self.isEmpty():
            raise ValueError("No animals in shelter!")
        else:
            for i in range(self.animalCount()):
                if self.main[i] == 'DOG':
                    return self.main.pop(i)
            raise ValueError('No DOGs found')

    def dequeueCAT(self):
        if self.isEmpty():
            raise ValueError("No animals in shelter!")
        else:
            for i in range(self.animalCount()):
                if self.main[i] == 'CAT':
                    return self.main.pop(i)
            raise ValueError('No CATs found')

    def animalCount(self):
        return len(self.main)

    def isEmpty(self):
        return len(self.main) == 0