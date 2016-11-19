# coding: utf8
import sys

import numpy as np
from load import *

def nonlin(x,deriv=False):
	if(deriv==True):
           return x*(1-x)

	return 1/(1+np.exp(-x))

# Обучающие данные    
# X = np.array([
#         [0,0,1],
#         [0,1,1],
#         [1,0,1],
#         [1,1,1]
#     ])

examples = len(collection)
exp_size = len(collection[0])
our_size = len(teacher[0])
#print our_size 
#sys.exit("Error message")
X = np.array(collection,dtype=int)

# Ответы для обучающей выборки из Х     
#y = np.array([[0,1,1,0]]).T
y = np.array(teacher,dtype=int)#.T

np.random.seed(1)
print y
# случайно инициализируем веса, в среднем - 0
syn0 = 2*np.random.random((exp_size,examples)) - 1
syn1 = 2*np.random.random((examples,our_size)) - 1
iterations = 12000
iter_step = 6000
for j in xrange(iterations):
	# проходим вперёд по слоям 0, 1 и 2
    l0 = X
    l1 = nonlin(np.dot(l0,syn0))
    l2 = nonlin(np.dot(l1,syn1))

    # как сильно мы ошиблись относительно нужной величины?
    #print l2
    l2_error = y - l2
    if (j% iter_step) == 0:
        print "Error:" + str(np.mean(np.abs(l2_error)))
        
    # в какую сторону нужно двигаться?
    # если мы были уверены в предсказании, то сильно менять его не надо
    l2_delta = l2_error*nonlin(l2,deriv=True)

    # как сильно значения l1 влияют на ошибки в l2?
    l1_error = l2_delta.dot(syn1.T)
    
    # в каком направлении нужно двигаться, чтобы прийти к l1?
    # если мы были уверены в предсказании, то сильно менять его не надо
    l1_delta = l1_error * nonlin(l1,deriv=True)

    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)

np.save('synapse/syn0.npy', syn0)
np.save('synapse/syn1.npy', syn1)

#print syn0
#print syn1