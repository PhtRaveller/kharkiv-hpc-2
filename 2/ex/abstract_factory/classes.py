#!/usr/bin/python

#This is Abstract factory
class AnimalFactory(object):
    def createAnimal(self, name):
        pass
    def createFood(self):
        pass
    def createHouse(self):
        pass
#Abstract classes
class Animal(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return "I'm {0} {1}\nI eat {2} and live in {3}"\
                .format(self.kind, self.name, self.food, self.house)
    def addFood(self, food):
        self.food = food
    def addHouse(self, house):
        self.house = house

class Food(object):
    def __repr__(self):
        return "{0}".format(self.kind)

class House(object):
    def __repr__(self):
        return "{0}".format(self.kind)

#Concrete classes
class Dog(Animal):
    kind = 'dog'

class DogFood(Food):
    kind = 'dog food'

class DogHouse(House):
    kind = 'dog house'

class Cat(Animal):
    kind = 'cat'

class CatFood(Food):
    kind = 'cat food'

class CatHouse(House):
    kind = 'cat house'

#Concrete factories
class DogFactory(AnimalFactory):
    def createAnimal(self, name):
        return Dog(name)
    def createFood(self):
        return DogFood()
    def createHouse(self):
        return DogHouse()

class CatFactory(AnimalFactory):
    def createAnimal(self, name):
        return Cat(name)
    def createFood(self):
        return CatFood()
    def createHouse(self):
        return CatHouse()
