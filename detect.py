# coding: utf8

import numpy as np
from loadsample import *

np.set_printoptions(suppress=True)
def nonlin(x,deriv=False):
	if(deriv==True):
           return x*(1-x)

	return 1/(1+np.exp(-x))

#load sinapse
syn0 = np.load('synapse/syn0.npy')
syn1 = np.load('synapse/syn1.npy')

X = np.array(collection,dtype=float)

# проходим вперёд по слоям 0, 1 и 2
l0 = X
l1 = nonlin(np.dot(l0,syn0))
l2 = nonlin(np.dot(l1,syn1))

print teacher
print l2

#print syn0
#print syn1