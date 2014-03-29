#!/usr/bin/python

from integrators import EulerIntegrator
from observers import WritingObserver

class DynSystem(object):
    def __init__(self, initx, initp, params):
        self.x = initx
        self.p = initp
        if len(initx) != len(initp):
            raise ValueError
        self.dim = len(initx)
        self.observers = []
        self.params = params

    def represent(self):
        for i in range(self.dim):
            print "x{0}={1}, p{0}={2}".format(i, self.x[i], self.p[i])

    def force(self, time, x=None, p=None):
        pass

    def set_integrator(self, integrator):
        self.integrator = integrator

    def add_observer(self, observer):
        self.observers.append(observer)
        observer.add_subject(self)

    def integrate(self):
        for time in self.integrator.points():
            self.x, self.p = self.integrator.make_step(self)

            for observer in self.observers:
                if observer.event(time):
                    observer.update(time)

class Oscillator(DynSystem):

    def force(self, time, x=None, p=None):
        if x is None or p is None:
            x = self.x
            p = self.p
        elif len(x)!=self.dim or len(p)!=self.dim:
            raise ValueError("Wrong dimensions")
        xf = [pi for pi in p]
        pf = [-self.params[i]*self.params[i]*x[i] for i in range(self.dim)]
        return xf, pf

def main():
    ix = [1,]
    ip = [0,]
    ds = Oscillator(ix, ip, [1,])
    integ = EulerIntegrator(0.005, 50000, None)
    obs = WritingObserver(None)
    ds.add_observer(obs)
    ds.set_integrator(integ)
    ds.integrate()

if __name__ == '__main__':
    main()
