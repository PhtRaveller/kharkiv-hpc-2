#!/usr/bin/python

class Integrator(object):
    def __init__(self, step, nsteps, params):
        self.step = step
        self.params = params
        self.nsteps = nsteps
        self.time = 0
    def points(self):
        return ((i+1)*self.step for i in range(self.nsteps))
    def make_step(self, ds):
        pass

class EulerIntegrator(Integrator):
    def make_step(self, ds):        
        f = ds.force(self.time)
        x = [ds.x[i] + self.step * f[i] for i in range(len(f))]
        return x

class Runge2Order(Integrator):
    def make_step(self, ds):
        f= ds.force(self.time)
        x1 = [ds.x[i] + 0.5 * self.step * f[i] for i in range(len(f))]
        f = ds.force(self.time+0.5 * self.step, x1)
        x = [ds.x[i] + self.step * f[i] for i in range(len(f))]
        return x