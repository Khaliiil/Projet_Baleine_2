# -*- coding: utf-8 -*-
import aifc
import numpy as np
from numpy.fft import fft, rfft, fftfreq, fftshift
import matplotlib.pyplot as plt


f = open('C:\\Users\\AxllowFifty\\Desktop\\Samples\\train.csv')
data = np.loadtxt(f, dtype= str , delimiter = ',')
F = data[:0]                # 1ere colonne
T = data[:1]                # 2eme colonne

filename = 'C:\\Users\\AxllowFifty\\Desktop\\Samples\\train3.aiff'
s = aifc.open(filename, 'r')
nframes = s.getnframes() 
assert nframes == 4000 # on valide qu'on a bien nombre de points = 4000

strsig = s.readframes(nframes)
y = np.fromstring(strsig, np.short).byteswap()
f_s = s.getframerate() #fréquence d'échantillonnage
assert f_s == 2000 # on valide que c'est bien 2 kHz
y_fft = np.fft.fft(y)

#plt.plot(y_fft)
#plt.show()

Delta_T = 1./f_s # Delta temps entre samples
N=nframes
#ampl = 1/N * np.abs(y_fft)
ampl = np.abs(y_fft)*1./N
freqs = np.fft.fftfreq(N, Delta_T)
plt.plot(freqs, ampl)
plt.plot(freqs[:N/2], ampl[:N/2])
