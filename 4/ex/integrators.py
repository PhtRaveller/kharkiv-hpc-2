#!/usr/bin/python

class Integrator(object):
    def __init__(self, step, nsteps, params):
        self.step = step
        self.params = params
        self.nsteps = nsteps
        self.time = 0
    def points(self):
        return ((i+1)*self.step for i in range(self.nsteps))
    def make_step(self, dynsys):
        pass

class EulerIntegrator(Integrator):
    def make_step(self, dynsys):        
        xf, pf = dynsys.force(self.time)
        x = [dynsys.x[i] + self.step * xf[i] for i in range(len(xf))]
        p = [dynsys.p[i] + self.step * pf[i] for i in range(len(xf))]        
        return x, p