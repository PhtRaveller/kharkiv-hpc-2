#!/usr/bin/python

import rec
import numpy as np
import time
from config import cfg
from array import array
import matplotlib
from matplotlib import pyplot as plt
matplotlib.rc('font', family='monospace')

def benchmark(func):
    fname = 'data.npy'
    d = np.load(fname)
    if f is rec.rec_list:
        d = d.tolist()
    elif f is rec.rec_array:
        d = array('d', d.tolist())
    for i in range(1, cfg['num_divs']+1):
        t = 0.
        N = len(d) * i / cfg['num_divs']
        res = np.zeros((N,N), dtype=np.uint8)
        for n in range(cfg['num_runs']):
            wd = d[:N]
            t0 = time.clock()
            func(wd, res, cfg['thresh'])
            t += time.clock() - t0
        t /= n+1
        print '{} {}'.format(N, t)
    np.save('rp.npy', res)

def plot_all():
    import os
    files = [s for s in os.listdir('.') if s[-4:]=='.dat']
    for f in files:
        data = np.loadtxt(f, delimiter=' ', dtype=float)
        plt.plot(data[:,0], data[:, 1], label=f[:-4])
    plt.legend(loc=2, fontsize=12)
    plt.grid()
    plt.show()

if __name__ == '__main__':
    import sys
    if 'bench' in sys.argv:
        if 'array' in sys.argv:
            f = rec.rec_array
        elif 'numpy' in sys.argv:
            f = rec.rec_numpy
        elif 'ctypes' in sys.argv:
            f = rec.rec_ctypes
        elif 'blocked' in sys.argv:
            f = rec.rec_blocked
        else:
            f = rec.rec_list
        benchmark(f)
    elif 'plot' in sys.argv:
        plot_all()
