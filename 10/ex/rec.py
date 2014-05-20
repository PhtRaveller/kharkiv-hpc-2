#!/usr/bin/python

import numpy as np
import ctypes as ct
lib = ct.cdll['./libfuncs.so']
crec = lib.rec
crec.argtypes = [ct.POINTER(ct.c_double), ct.POINTER(ct.c_byte), ct.c_double, ct.c_int]
crec_blocked = lib.rec_blocked
crec_blocked.argtypes = [ct.POINTER(ct.c_double), ct.POINTER(ct.c_byte), ct.c_double, ct.c_int]
# crec = lib.rec
# crec.argtypes = [ct.POINTER(ct.c_double), ct.POINTER(ct.c_byte), ct.c_int]


def rec_list(s, res, thresh):
    for i in range(len(s)):
        for j in range(i, len(s)):
            res[i,j] = abs(s[i]-s[j]) < thresh

def rec_array(s, res, thresh):
    rec_list(s, res, thresh)

def rec_numpy(s, res, thresh):
    for i in range(len(s)):
        res[i, i:] = np.abs(s[i:]-s[i]) < thresh

def rec_ctypes(s, res, thresh):
    crec(s.ctypes.data_as(ct.POINTER(ct.c_double)),
        res.ctypes.data_as(ct.POINTER(ct.c_byte)), ct.c_double(thresh), len(s))

def rec_blocked(s, res, thresh):
    crec(s.ctypes.data_as(ct.POINTER(ct.c_double)),
        res.ctypes.data_as(ct.POINTER(ct.c_byte)), ct.c_double(thresh), len(s))
