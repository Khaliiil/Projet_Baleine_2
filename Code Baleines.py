# -*- coding: utf-8 -*-
#Khalil MAHFOUDH

import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
import scipy
import aifc
import csv
import pandas as pd
import sys

# Chargement des bibliothèques Qt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QGridLayout, QInputDialog, QFrame
from PyQt5.QtGui import QFont, QPixmap


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
while len(not_whale) != 1000:
    if df['label'][i] == 0:
        not_whale.append(df['sample'][i])
        #création de la liste des 0
        label.append(0)
    i += 1
    
i = 0
while len(whale) != 1000:
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
        s = aifc.open('C:\\Users\\charpak2.21\\Desktop\\Projet_Baleine\\train\\' + filename, "r")
        N = s.getnframes()
        strsig = s.readframes(N)
        y = np.fromstring(strsig, np.short).byteswap()
        FE = s.getframerate()
        A = np.fft.fft(y)

        DeltaT = 1./FE
        ampl = np.abs(A)*1./N
        freqs = np.fft.fftfreq(N, DeltaT)
        if len(liste) == 1:
            P = plt.plot(freqs[:N/2], ampl[:N/2]) 
            plt.ylabel("Amplitude")
            plt.xlabel("Frequence")
            plt.show()
        liste_sample_fft.append(ampl)
    #return P
    return liste_sample_fft


a = fct_FFT(not_whale)
b = fct_FFT(whale)
liste_finale = a + b
#print len(label)
#print len(liste_finale)


from sklearn.ensemble import RandomForestClassifier
#machine learning en apprenant à classifier les types de baleines
B = RandomForestClassifier()
B.fit(liste_finale, label)

#print (B.predict(liste_finale[1].reshape(1, -1)))

#Z = ['train25698.aiff']
#print fct_FFT (Z)
#print (B.predict(fct_FFT (Z)))



class FenetreDessin(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Détéction de Baleines")
        
        self.setCentralWidget(QFrame())
        self.pic = QLabel(self)
        self.pic.setPixmap(QPixmap("C:\\Users\\charpak2.21\\Desktop\\Projet_Baleine\\baleine.jpg"))
        self.pic.setGeometry(0, 0, 600, 600)
        
        self.texte = QLabel(("                                                Bienvenue sur le détécteur de baleine !\n                        Cliquer sur Entrer lorsque vous souhaitez commencer la détéction..."), self)  
        self.texte.setFont(QFont("Times New Roman", 12))
        self.texte.setStyleSheet('color: black')

        self.bouton = QPushButton("Entrer", self.centralWidget())
        self.bouton.clicked.connect(self.fonctionB)

        self.setGeometry(375, 125, 50, 50)
        posit = QGridLayout()
        posit.addWidget(self.pic, 0, 0)
        posit.addWidget(self.texte, 1, 0)
        posit.addWidget(self.bouton, 2, 0)
        self.centralWidget().setLayout(posit)
        
    def fonctionB(self):
        """Lance la deuxième fenêtre"""
        text, ok = QInputDialog.getText(self, 'Fichier son',
            'Veuillez entrez le nom du fichier son (format aiff) :')
        if ok:
            fichier = str(text)
            fichier = [fichier]
            a = B.predict(fct_FFT (fichier))
            if a == [1]:
                plt.title("Baleine detectee !!!", fontsize = 20, color = "green")
                print "Baleine detectee !!!"
            else:
                plt.title("Pas de baleine en vue...", fontsize = 20, color = "red")
                print "Pas de baleine en vue..."


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    fenetre = FenetreDessin()
    fenetre.show()                                                                                  #On rend visible la fenêtre.
    
    app.exec_()
