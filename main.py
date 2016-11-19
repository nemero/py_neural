# coding: utf8

import numpy as np

# Сигмоида 
def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))
    
# набор входных данных
X = np.array([  [0,0,1],
                [0,1,1],
                [1,0,1],
                [1,1,1] ])
    
# выходные данные            
y = np.array([[0,1,1,1]]).T
print y
# сделаем случайные числа более определёнными
np.random.seed(1)

# инициализируем веса случайным образом со средним 0
syn0 = 2*np.random.random((3,1)) - 1
print syn0
for iter in xrange(10000):

    # прямое распространение
    l0 = X
    l1 = nonlin(np.dot(l0,syn0))
    # if iter % 2500 == 0:
    #     print l1
    # насколько мы ошиблись?
    l1_error = y - l1
    if iter % 2500 == 0:
        print 'Match '
        print l1_error
    # перемножим это с наклоном сигмоиды 
    # на основе значений в l1
    l1_delta = l1_error * nonlin(l1,True) # !!!

    # обновим веса
    if iter % 2500 == 0:
        print 'info L0'
        print l0.T

        print 'Info l1 delta'
        print l1_delta


    syn0 += np.dot(l0.T,l1_delta) # !!!

print "Выходные данные после тренировки:"
print l1