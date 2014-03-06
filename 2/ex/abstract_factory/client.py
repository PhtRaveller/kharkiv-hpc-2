#!/usr/bin/python

from classes import DogFactory, CatFactory

def main():
    import sys
    factory = None
    if '-n' in sys.argv:
        name = sys.argv[sys.argv.index('-n')+1]
    else:
        name = 'default'
    if '-c' in sys.argv: 
        factory = CatFactory()
    elif '-d' in sys.argv:
        factory = DogFactory()
    if factory:
        animal = factory.createAnimal(name)
        food = factory.createFood()
        house = factory.createHouse()
        animal.addFood(food)
        animal.addHouse(house)
    print animal

if __name__ == '__main__':
    main()