# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
import scipy
import aifc
import csv
import pandas as pd


#ouverture du fichier
df = pd.read_csv('train.csv', header=0, sep=',')
#nomination des colonnes
df.columns=['sample', 'label']

#création de deux listes, propres aux baleines franches et non baleines franches
whale = list()
not_whale = list()
#liste dans laquelle on rentre les o ou 1
label = list()

i = 0
#liste de longueur 500 où les non baleines (label=0) sont dedans
while len(not_whale) != 500:
    if df['label'][i] == 0:
        not_whale.append(df['sample'][i])
        #création de la liste des 0
        label.append(0)
    i += 1
    
i = 0
while len(whale) != 500:
    if df['label'][i] == 1:
        whale.append(df['sample'][i])
        #création de la liste des 1
        label.append(1)
    i += 1

#print label
#print (len(not_whale))
#print not_whale

#création de la liste 

#x = not_whale[i]

def fct_FFT (liste) :
    liste_sample_fft = list()
    for i in range (len(liste)) :
        filename = liste[i]
        s = aifc.open("C:\\Users\\Orianne\\Desktop\\autre git\\whale_data\\data\\train\\" + filename, "r")
        N = s.getnframes()
        strsig = s.readframes(N)
        y = np.fromstring(strsig, np.short).byteswap()
        FE = s.getframerate()
        A = np.fft.fft(y)

        DeltaT = 1./FE
        ampl = np.abs(A)*1./N
        freqs = np.fft.fftfreq(N, DeltaT)
        
        P = plt.plot(freqs[:N/2], ampl[:N/2]) 
        plt.ylabel("Amplitude")
        plt.xlabel("Frequence")
        #plt.show()
        liste_sample_fft.append(ampl)
    #return P
    return liste_sample_fft


a = fct_FFT(not_whale)
b = fct_FFT(whale)
liste_finale = a + b


from sklearn.ensemble import RandomForestClassifier
#machine learning en apprenant à classifier les types de baleines
B = RandomForestClassifier()
B.fit(liste_finale, label)

print (B.predict(liste_finale[1].reshape(1, -1)))

Z = ['train25698.aiff']
print fct_FFT (Z)
print (B.predict(fct_FFT (Z)))
