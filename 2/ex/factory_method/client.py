#!/usr/bin/python

from classes import Zoo

def main():
    import sys
    zoo = Zoo('RandaZoo')
    if '-k' in sys.argv:
        kind = sys.argv[sys.argv.index('-k')+1]
        if '-n' in sys.argv:
            name = sys.argv[sys.argv.index('-n')+1]
        else:
            name = 'default'
        animal = zoo.createAnimal(kind, name)
        zoo.addAnimal(animal)
    zoo.representZoo()

if __name__ == '__main__':
    main()
