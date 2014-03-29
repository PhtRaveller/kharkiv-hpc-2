#!/usr/bin/python

from integrators import Runge2Order
from observers import WritingObserver

# "Abstract" class for dynamical system
class DynSystem(object):
    '''"Abstract" class representing dynamical system.'''
    def __init__(self, initx, params):
        self.x = initx
        self.dim = len(initx)
        self.observers = []
        self.params = params

    def represent(self):
        '''Template method for printing information about a system. Override it
        in subclasses.'''
        pass
        

    def force(self, time, x=None):
        '''Template method, which calculates forces. Override it in subclasses.'''
        pass

    def set_integrator(self, integrator):
        self.integrator = integrator

    def add_observer(self, observer):
        self.observers.append(observer)
        observer.add_subject(self)

    def integrate(self):
        '''Integration method. Proceeds one step using integrator (Strategy pattern),
        checks for event for each observer and updates observers if necessary
        (Observer pattern).'''
        for time in self.integrator.points():
            self.x = self.integrator.make_step(self)

            for observer in self.observers:
                if observer.event(time):
                    observer.update(time)

# Concrete classes for dynamical systems
class Oscillator(DynSystem):
    '''Concrete class for harmonic oscillator.'''
    def represent(self):
        for i in range(self.dim/2):
            print "x{0}={1}, p{0}={2}".format(i, self.x[i], self.x[i+self.dim/2])
    def force(self, time, x=None):
        if x is None:
            x = self.x
        xf = [pi for pi in x[self.dim/2:]]
        pf = [-self.params[i]*self.params[i]*x[i] for i in range(self.dim/2)]
        return xf + pf

class LorenzSystem(DynSystem):
    '''Concrete class for Lorenz system.'''
    def force(self, time, x=None):
        if x is None:
            x = self.x
        f1 = self.params[0] * (x[1] - x[0])
        f2 = x[0] * (self.params[1] - x[2]) - x[1]
        f3 = x[0] * x[1] - self.params[2] * x[2]
        return [f1, f2, f3]

    def represent(self):
        print "X={0}, Y={1}, Z={2}, sigma={3}, ro={4}, beta={5}".format(*(self.x+self.params))

def lorenz():
    ix = [0.2,0.2,20.]
    params = [10.,  28., 8./3.]
    ds = LorenzSystem(ix, params)
    integ = Runge2Order(0.005, 20000, None)
    obs = WritingObserver(None)
    ds.add_observer(obs)
    ds.set_integrator(integ)
    ds.integrate()

def osc():
    ix = [1., 0., 0., 1.]
    params = [1., 1.4]
    ds = Oscillator(ix, params)
    integ = Runge2Order(0.005, 10000, None)
    obs = WritingObserver(None)
    ds.add_observer(obs)
    ds.set_integrator(integ)
    ds.integrate()

if __name__ == '__main__':
    import sys
    if '-l' in sys.argv:
        lorenz()
    else:
        osc()
