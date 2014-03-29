#!/usr/bin/python

# "Abstract" observer class
class Observer(object):
    def __init__(self, params):
        self.params = params
        self.subjects = []
        self.init_me()

    def add_subject(self, subject):
        self.subject = subject

    def event(self, time):
        '''Method, which determines, whether event happened. Override in subclasses.
        (Template pattern).'''
        pass

    def init_me(self):
        '''Method, which performs additional initialization if necessary.
        Override in subclasses. (Template pattern).'''
        pass

    def update(self, time):
        '''Method, which updates observer. Override in subclasses. (Template pattern).'''
        pass

# Concrete observer classes
class WritingObserver(Observer):
    '''Observer, which outputs coordinates to console.'''
    def event(self, time):
        '''Since we want to output coordinates at each step, we return True always.'''
        return True

    def update(self, time):
        s = "{:f} " * self.subject.dim
        print s.format(*self.subject.x)