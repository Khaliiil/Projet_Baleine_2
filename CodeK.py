# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import scipy
import aifc


#MISE EN NUMPY DU SON

filename = "test7.aiff"
s = aifc.open("C:\\Users\\Orianne\\Documents\\projet\\whale_data\\data\\test\\" + filename, 'r')
nframes = s.getnframes()
strsig = s.readframes(nframes)
y = np.fromstring(strsig, np.short).byteswap()
print y    
type(y)


#FFT ET VISUALISATION DU SON



n = 40

# definition de a

y[1] = 1

# visualisation de a
# on ajoute a droite la valeur de gauche pour la periodicite
plt.subplot(311)
plt.plot( np.append(y, y[0]) )

# calcul de A
A = np.fft.rfft(y)
type(A)

# visualisation de A
# on ajoute a droite la valeur de gauche pour la periodicite
"""B = np.append(A, A[0])
plt.subplot(312)
plt.plot(np.real(B))
plt.ylabel("partie reelle")

plt.subplot(313)
plt.plot(np.imag(B))
plt.ylabel("partie imaginaire")"""

#plt.show()





#Spectrogramme

plt.figure(figsize=(18.,12.))
#filename = "test4.aiff"
f = aifc.open("C:\\Users\\Orianne\\Documents\\projet\\whale_data\\data\\test\\" + filename, 'r')

str_frames = f.readframes(f.getnframes())
Fs = f.getframerate()
time_data = np.fromstring(str_frames, np.short).byteswap()
f.close()

# spectrogram of file
Pxx, freqs, bins, im = plt.specgram(time_data,Fs=Fs,noverlap=90,cmap=plt.cm.gist_heat)
#plt.title(filename+' fr'+filename_to_labels[filename])
plt.show()
