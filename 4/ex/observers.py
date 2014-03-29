#!/usr/bin/python

class Observer(object):
    def __init__(self, params):
        self.params = params
        self.subjects = []
        self.init_me()

    def add_subject(self, subject):
        self.subject = subject

    def event(self, time):
        pass

    def init_me(self):
        pass

    def update(self, time):
        pass

class WritingObserver(Observer):
    def event(self, time):
        return True

    def update(self, time):
        s = "{:f} {:f} " * self.subject.dim
        print s.format(*(self.subject.x+self.subject.p))