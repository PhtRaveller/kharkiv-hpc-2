#!/usr/bin/python

class Zoo(object):
    '''Main class. Represents zoo, to which one can add animals.'''
    def __init__(self, name):
        self.name = name
        self.animals = []
    def addAnimal(self, animal):
        '''Adds animals to the zoo.'''
        self.animals.append(animal)
    def createAnimal(self, kind, animal_name):
        '''This is factory method. Creates animals.'''
        if kind == 'lion':
            return Lion(animal_name)
        elif kind == 'penguin':
            return Penguin(animal_name)
        elif kind == 'zebra':
            return Zebra(animal_name)
        else:
            print "I do not know this animal!"
    def representZoo(self):
        print "This is %s zoo. Animals:" % self.name
        if not self.animals:
            print "No animals yet"
        for a in self.animals:
            print a

class Animal(object):
    name = ''
    kind = ''
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return "I'm {0} {1}".format(self.kind, self.name)

class Lion(Animal):
    kind = 'lion'

class Penguin(Animal):
    kind = 'penguin'
    
class Zebra(Animal):
    kind = 'zebra'