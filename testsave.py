import numpy as np
from tempfile import TemporaryFile

outfile = TemporaryFile()
syn0 = 'synapse/syn0.npy'
x = np.arange(10)
np.save(syn0, x)
print np.load(syn0)