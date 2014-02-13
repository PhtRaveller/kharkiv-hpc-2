#!/usr/bin/python

import numpy as np

def get_info(data):
    '''Returns mean, STD and max element for the ``data``.

    Parameters
    ==========
    data : ``numpy`` array
        Data series for analysis

    Returns
    =======
    out : tuple
        Tuple of mean, STD and max element from ``data``.
    '''

    return data.mean(), data.std(), data.max()

def get_info_file(filename):
    '''Reads data file and returns data info.

    Parameters
    ==========
    filename : str
        Name of a file to read data from.

    Returns
    =======
    out : tuple
        Tuple of mean, STD and max element for data from ``filename``.
    '''

    data = np.loadtxt(filename)
    return get_info(data)

def get_info_str(datastr):
    '''Reads string of space separated values and returns data info.

    Parameters
    ==========
    datastr : str
        String with data ("x1 x2 ...").

    Returns
    =======
    out : tuple
        Tuple of mean, STD and max element for data from ``datastr``.
    '''

    data = np.array([float(x) for x in datastr.split(' ')])
    return get_info(data)

def main():
    import sys
    if '-f' in sys.argv:
        return get_info_file(sys.argv[-1])
    elif '-s' in sys.argv:
        return get_info_str(sys.argv[-1])

if __name__ == '__main__':
    result = main()
    print "Mean is {0}\nSTD is {1}\nMax element is {2}".format(*result)
