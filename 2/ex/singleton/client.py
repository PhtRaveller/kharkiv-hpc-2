#!/usr/bin/python

from classes import Singleton

def main():
    s1 = Singleton(1,2)
    f1 = s1.getInstance()
    s2 = Singleton(5,6)
    f2 = s2.getInstance()
    print f1 is f2

if __name__ == '__main__':
    main()