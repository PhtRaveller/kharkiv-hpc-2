#!/usr/bin/python

class Adaptee(object):
    def __init__(self, name):
        self.name = name
    def speak(self):
        print "I'm {}".format(self.name)

class Adapter(object):
    def __init__(self, name):
        self.adaptee = Adaptee(name)
    def tell_about(self):
        self.adaptee.speak()

class Client(object):
    def ask(self, adapter):
        adapter.tell_about()

if __name__ == '__main__':
    adapter = Adapter('Mike')
    client = Client()
    client.ask(adapter)        